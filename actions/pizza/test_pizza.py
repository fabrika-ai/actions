from fastapi.testclient import TestClient
from actions.pizza.main import app


client = TestClient(app)

def test_record_calories_success():
    """
    Test the /record-calories endpoint for a successful response.
    """
    response = client.post("/record-calories", json={"calories": 500})
    assert response.status_code == 200
    assert "Remaining calories for the day" in response.json().get("Message", "")

def test_record_calories_exceed_limit():
    """
    Test the /record-calories endpoint for exceeding the calorie limit.
    """
    response = client.post("/record-calories", json={"calories": 2000})
    assert response.status_code == 200
    assert response.json() == {"Error": "Calorie limit exceeded"}

def test_find_pizza_success():
    """
    Test the /find-pizza endpoint for a successful response.
    """
    response = client.get("/find-pizza")
    assert response.status_code == 200
    assert "Pizza" in response.json()

def test_find_pizza_failure():
    """
    Test the /find-pizza endpoint for a situation where no pizza fits the calorie limit.
    """
    # Record enough calories to exceed the limit
    client.post("/record-calories", json={"calories": 2000})
    response = client.get("/find-pizza")
    assert response.status_code == 404
    assert response.json() == {"detail": "No pizza fits the remaining calorie limit"}

def test_order_pizza_success():
    """
    Test the /order-pizza endpoint for a successful response.
    """
    response = client.post("/order-pizza", json={"pizza_name": "Margherita"})
    assert response.status_code == 200
    assert response.json() == {"Message": "Ordered a Margherita pizza!"}

def test_order_pizza_failure():
    """
    Test the /order-pizza endpoint with an invalid pizza name.
    """
    response = client.post("/order-pizza", json={"pizza_name": "Unknown"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Pizza not found"}
