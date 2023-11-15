from fastapi import FastAPI, HTTPException
from typing import Dict

import functions_framework
from helpers.utils import as_cloud_function

app = FastAPI()

# Globals
DAILY_CALORIE_LIMIT = 2000  # Set your daily calorie limit
daily_calories = 0
pizzas = {
    "Margherita": 300,
    "Pepperoni": 400,
    "Veggie": 350,
    "Hawaiian": 380
}

@app.post("/record-calories")
async def record_calories(calories: int):
    global daily_calories
    if daily_calories + calories > DAILY_CALORIE_LIMIT:
        return {"Error": "Calorie limit exceeded"}
    daily_calories += calories
    remaining_calories = DAILY_CALORIE_LIMIT - daily_calories
    return {"Message": f"Calories recorded. Remaining calories for the day: {remaining_calories}"}

@app.get("/find-pizza")
async def find_pizza():
    for pizza, cal in pizzas.items():
        if daily_calories + cal <= DAILY_CALORIE_LIMIT:
            return {"Pizza": pizza, "Calories": cal}
    raise HTTPException(status_code=404, detail="No pizza fits the remaining calorie limit")

@app.post("/order-pizza")
async def order_pizza(pizza_name: str):
    if pizza_name not in pizzas:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return {"Message": f"Ordered a {pizza_name} pizza!"}

@app.get("/hello-world")
async def get_user_name():
    return {"Hello": "World"}

@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
