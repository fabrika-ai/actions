from fastapi.testclient import TestClient
from actions.pizza.main import app


client = TestClient(app)

def test_record_calories_success():
    response = client.post("/record-calories", json={"calories": 500})
    assert response.status_code == 200
    assert "Remaining calories for the day" in response.json().get("Message", "")

def test_record_calories_exceed_limit():
    response = client.post("/record-calories", json={"calories": 2000})
    assert response.status_code == 200
    assert response.json() == {"Error": "Calorie limit exceeded"}

def test_find_pizza_failure():
    client.post("/record-calories", json={"calories": 2000})
    response = client.get("/find-pizza")
    assert response.status_code == 404
    assert response.json() == {"detail": "No pizza fits the remaining calorie limit"}

def test_order_pizza_success():
    response = client.post("/order-pizza", json={"pizza_name": "Margherita"})
    assert response.status_code == 200
    assert response.json() == {"Message": "Ordered a Margherita pizza!"}

def test_order_pizza_failure():
    response = client.post("/order-pizza", json={"pizza_name": "Unknown"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Pizza not found"}
