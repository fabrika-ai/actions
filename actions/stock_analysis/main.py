from fastapi import FastAPI
import functions_framework
import requests
from helpers.utils import as_cloud_function

app = FastAPI()

@app.get("/check-stock")
async def check(analysis_type : str, ticker : str):
    # possible actions for analysis_type = ['earnings-history, earnings-estimate']

    url = f"https://stock-analysis.p.rapidapi.com/api/v1/resources/{analysis_type}"
    querystring = {"ticker":ticker}

    headers = {
        "X-RapidAPI-Key": "d7e8ace26cmshb9d937b6e6fd092p163b93jsn7f3cdafcdc04",
        "X-RapidAPI-Host": "stock-analysis.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

print(response.json())

@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
