import json
from fastapi import FastAPI, HTTPException
from typing import Dict, List, Optional, Union

import functions_framework
from helpers.utils import as_cloud_function

from pydantic import BaseModel


app = FastAPI()


def load_diet():
    try:
        with open("diet.json", "r") as f:
            diet = Diet(**json.load(f))
    except FileNotFoundError:
        diet = None
    return diet


def load_meals():
    try:
        with open("meals.json", "r") as f:
            meals = [Meal(**meal) for meal in json.load(f)]
    except FileNotFoundError:
        meals = []
    return meals


def save_diet(diet):
    if diet is not None:
        with open("diet.json", "w") as f:
            json.dump(diet.dict(), f)


def save_meals(meals):
    with open("meals.json", "w") as f:
        json.dump([meal.dict() for meal in meals], f)


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


class MealsSummary(BaseModel):
    total_calories: int
    total_fats: int
    total_proteins: int
    total_carbohydrates: int
    meals: List[str]
    remaining_calories: int
    remaining_fats: int
    remaining_proteins: int
    remaining_carbohydrates: int


# Globals


@app.post("/diet")
async def set_current_diet(new_diet: Diet):
    save_diet(new_diet)
    return {"Message": f"Diet set successfully."}


@app.get("/diet")
async def get_current_diet():
    diet = load_diet()
    if diet is None:
        raise HTTPException(status_code=404, detail="Diet not set")
    return diet


@app.post("/meal")
async def add_meal(meal: Meal):
    meals = load_meals()
    meals.append(meal)
    save_meals(meals)
    return {"Message": f"Meal {meal.title} added successfully."}


@app.get("/meal")
async def get_meals() -> MealsSummary:
    daily_meal_history = load_meals()
    diet = load_diet()
    if len(daily_meal_history) == 0:
        raise HTTPException(status_code=404, detail="No meals recorded")

    if diet is None:
        raise HTTPException(status_code=404, detail="Diet not set")

    total_calories = sum(meal.calories_amount for meal in daily_meal_history)
    total_fats = sum(meal.fats_grams for meal in daily_meal_history)
    total_proteins = sum(meal.proteins_grams for meal in daily_meal_history)
    total_carbohydrates = sum(meal.carbohydrates_grams for meal in daily_meal_history)
    meals = [meal.title for meal in daily_meal_history]

    remaining_calories = diet.calories_restriction - total_calories
    remaining_fats = diet.fats_restriction_grams - total_fats
    remaining_proteins = diet.proteins_restriction_grams - total_proteins
    remaining_carbohydrates = diet.calories_restriction - total_carbohydrates

    return MealsSummary(
        total_calories=total_calories,
        total_fats=total_fats,
        total_proteins=total_proteins,
        total_carbohydrates=total_carbohydrates,
        meals=meals,
        remaining_calories=remaining_calories,
        remaining_fats=remaining_fats,
        remaining_proteins=remaining_proteins,
        remaining_carbohydrates=remaining_carbohydrates,
    )


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
