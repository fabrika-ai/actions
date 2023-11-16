from fastapi import FastAPI, HTTPException
from typing import Dict, List, Optional

import functions_framework
from helpers.utils import as_cloud_function

from pydantic import BaseModel


app = FastAPI()


## Diet
class Diet(BaseModel):
    prohibited_foods: List[str]
    recommended_foods: List[str]
    not_recommended_foods: List[str]
    cabrohydrates_restriction_grams: int
    cabrohydrates_restriction_description: str
    proteins_restriction_grams: int
    proteins_restriction_description: str
    fats_restriction_grams: int
    fats_restriction_description: str
    calories_restriction: int
    calories_restriction_description: str


class Meal(BaseModel):
    title: str
    fats_grams: int
    proteins_grams: int
    carbohydrates_grams: int
    calories_amount: int
    products: List[str]


# Globals
DAILY_CALORIE_LIMIT = 2000  # Set your daily calorie limit
diet = None
daily_meal_history: List[Meal] = []


@app.post("/diet")
async def set_current_diet(new_diet: Diet):
    global diet
    diet = new_diet
    return {"Message": f"Diet set successfully."}


@app.get("/diet")
async def get_current_diet():
    global diet
    if diet is None:
        raise HTTPException(status_code=404, detail="Diet not set")
    return diet


@app.post("/meal")
async def add_meal(meal: Meal):
    global daily_meal_history
    daily_meal_history.append(meal)
    return {"Message": f"Meal {meal.title} added successfully."}


@app.get("/meal")
async def get_meals():
    global daily_meal_history
    if not daily_meal_history:
        raise HTTPException(status_code=404, detail="No meals recorded")
    return daily_meal_history


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
