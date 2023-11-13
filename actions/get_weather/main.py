from fastapi import FastAPI
import functions_framework
import httpx

from helpers.utils import as_cloud_function

app = FastAPI()

# Define the Dark Sky API URL and headers
WEATHER_URL = f"http://api.weatherapi.com/v1/current.json?key=f615ff232b2448d1a8312353231311&q={}&aqi=no"

@app.get("/get_weather/{location}")
async def read_weather(location: str):
    response = requests.get(WEATHER_URL.format(location))
    return response.json()

@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)

