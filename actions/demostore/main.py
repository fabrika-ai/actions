import os
import random
import time
import uuid
from typing import List, Dict
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import functions_framework

from helpers.utils import as_cloud_function

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float


class AvailableProductsResponse(BaseModel):
    products: List[Product]


class OrderRequest(BaseModel):
    products: List[str]
    delivery_address: str


class OrderResponse(BaseModel):
    order_id: str
    total_cost: float
    delivery_address: str


class DeliveryCheckRequest(BaseModel):
    address: str


class DeliveryCheckResponse(BaseModel):
    available: bool


class TotalCostRequest(BaseModel):
    products: List[str]


class TotalCostResponse(BaseModel):
    total_cost: float


# Sample product list
products_list = {
    "Milk": 12.0,
    "Bread": 3.5,
    "Eggs": 5.0,
    "Cheese": 10.0,
    "Butter": 4.0
}


def get_total_cost(products: List[str]) -> float:
    """
    Calculate the total cost of the given list of products.

    Args:
        products (List[str]): A list of product names.

    Returns:
        float: The total cost of the products.
    """
    total_cost = 0
    for product in products:
        if product not in products_list:
            raise ValueError(f"Product '{product}' not found")
        total_cost += products_list[product]
    return total_cost


@app.get("/get-products", response_model=AvailableProductsResponse, summary="Get Available Products")
async def get_products():
    """
    Retrieve the list of available products with their prices.

    Returns:
        dict: A dictionary of product names and their prices.
    """
    products = [
        Product(
            name=name,
            price=price
        )
        for name, price in products_list.items()
    ]
    return AvailableProductsResponse(products=products)


@app.post("/calculate-total-cost", response_model=TotalCostResponse, summary="Calculate Total Cost of Products")
async def calculate_total_cost(request: TotalCostRequest):
    """
    Calculate the total cost of a list of products.

    Args:
        request (TotalCostRequest): A list of product names to calculate the total cost.

    Returns:
        TotalCostResponse: The total cost of the products.
    """
    try:
        total_cost = get_total_cost(request.products)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return {"total_cost": total_cost}


@app.post("/order", response_model=OrderResponse, summary="Place an Order")
async def order(request: OrderRequest):
    """
    Create an order with a list of products and a delivery address.

    Args:
        request (OrderRequest): The order details including product names and delivery address.

    Returns:
        OrderResponse: The order ID, total cost, and delivery address of the order.
    """
    try:
        total_cost = get_total_cost(request.products)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return {
        "order_id": str(uuid.uuid4()),
        "timestamp": str(time.time()),
        "total_cost": total_cost,
        "delivery_address": request.delivery_address,
        "estimated_time": str(random.randint(10, 25)) + " minutes"
    }


@app.post("/check-delivery", response_model=DeliveryCheckResponse, summary="Check Delivery Availability")
async def check_delivery(request: DeliveryCheckRequest):
    """
    Check if delivery is available to a specific address.

    Args:
        request (DeliveryCheckRequest): The address to check for delivery availability.

    Returns:
        DeliveryCheckResponse: Information about delivery availability at the specified address.
    """
    available = True
    if "London" in request.address:
        available = False
    return {
        "available": available,
    }


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
