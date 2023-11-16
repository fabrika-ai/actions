from fastapi.testclient import TestClient

from actions.template.main import app

client = TestClient(app)


def test_diet_endpoint():
    """
    Test the /diet endpoint for a successful response.
    """
    diet_data = {
        "prohibited_foods": ["Pizza"],
        "recommended_foods": ["Salad"],
        "not_recommended_foods": ["Burger"],
        "cabrohydrates_restriction_grams": 100,
        "proteins_restriction_grams": 50,
        "fats_restriction_grams": 30,
        "calories_restriction": 2000,
    }
    response = client.post("/diet", json=diet_data)
    assert response.status_code == 200
    assert response.json() == {"Message": "Diet set successfully."}


def test_meal_endpoint():
    """
    Test the /meal endpoint for a successful response.
    """
    meal_data = {
        "title": "Lunch",
        "fats_grams": 10,
        "proteins_grams": 20,
        "carbohydrates_grams": 30,
        "calories_amount": 500,
        "products": ["Chicken", "Rice"],
    }
    response = client.post("/meal", json=meal_data)
    assert response.status_code == 200
    assert response.json() == {"Message": "Meal Lunch added successfully."}


def test_get_diet_endpoint():
    """
    Test the /diet endpoint for getting the diet.
    """
    response = client.get("/diet")
    assert response.status_code == 200


def test_get_meal_endpoint():
    """
    Test the /meal endpoint for getting the meals.
    """
    response = client.get("/meal")
    assert response.status_code == 200
