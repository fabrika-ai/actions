from fastapi.testclient import TestClient
from actions.pizza.main import app

client = TestClient(app)

def test_record_calories_success():
    """
    Test the /record-calories endpoint for a successful response.
    """
    response = client.post("/record-calories", json={"calories": 500})
    print(response.status_code)

    assert response.status_code == 200
    assert "Remaining calories for the day" in response.json().get("Message", "")

def test_record_calories_exceed_limit():
    """
    Test the /record-calories endpoint for exceeding the calorie limit.
    """
    # Assuming the daily limit is 2000 and we already recorded 500 calories
    response = client.post("/record-calories", json={"calories": 1600})
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
    # Assuming the daily limit is already exceeded or very close to being exceeded
    response = client.get("/find-pizza")
    assert response.status_code == 404

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
