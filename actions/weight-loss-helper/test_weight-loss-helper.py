from fastapi.testclient import TestClient
from actions.weight-loss-helper.main import app  # Replace with your actual FastAPI app import

client = TestClient(app)

def test_store_record_success():
    """
    Test the /store_record endpoint for a successful response.
    """
    # Sample data for testing
    test_data = {"datetime": "2023-11-12T12:00:00", "calories": 500}
    
    response = client.post("/store_record", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Record stored successfully"}

def test_store_record_invalid_request():
    """
    Test the /store_record endpoint with invalid request data.
    """
    # Invalid data (e.g., missing fields or wrong data type)
    invalid_data = {"datetime": "2023-11-12T12:00:00"}  # Missing 'calories'

    response = client.post("/store_record", json=invalid_data)
    # Expecting a 422 Unprocessable Entity for invalid data
    assert response.status_code == 422

def test_store_record_response_structure():
    """
    Test to ensure the response structure from /store_record is as expected.
    """
    test_data = {"datetime": "2023-11-12T12:00:00", "calories": 500}

    response = client.post("/store_record", json=test_data)
    assert response.status_code == 200
    # Verifying the exact structure of the response
    assert response.json() == {"message": "Record stored successfully"}

# You can add more tests here for different scenarios and edge cases
