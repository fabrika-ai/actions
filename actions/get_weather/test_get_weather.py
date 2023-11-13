from fastapi.testclient import TestClient

from actions.get_weather.main import app

client = TestClient(app)


def test_endpoint_success():
    """
    Test the endpoint for a successful response.
    Replace '/hello-world' with the actual endpoint you are testing.
    """
    response = client.get("/get_weather")  # Use the appropriate HTTP method (get, post, etc.)
    assert response.status_code == 200
    # Add more assertions here to validate the response content if needed


def test_endpoint_invalid_request():
    """
    Test the endpoint with an invalid request.
    Adjust the request parameters and the expected response code as needed.
    """
    # Example for a GET request with invalid parameters
    response = client.get("/get_weather/invalid_place123")  # Modify as per your endpoint
    assert response.status_code == 1006  # Replace with the expected status code for an invalid request (ex. 400)


def test_get_weather_response_structure():
    """
    Test to ensure the /get_weather response structure is as expected.
    This is important for endpoints where the response structure is crucial.
    """
    # Replace with a valid location for the test
    response = client.get("/get_weather/Moscow")
    assert response.status_code == 200
    response_data = response.json()

    # Assertions to check the structure of the response
    assert "location" in response_data
    assert "current" in response_data
    # Further assertions can be added to check the structure in more detail
    assert isinstance(response_data["location"], dict)
    assert isinstance(response_data["current"], dict)

    # Example: Verifying some key fields in the response
    assert "name" in response_data["location"]
    assert "temp_c" in response_data["current"]
    assert "condition" in response_data["current"]
    assert isinstance(response_data["current"]["condition"], dict)
    assert "text" in response_data["current"]["condition"]