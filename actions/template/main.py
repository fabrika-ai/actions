from fastapi import FastAPI
import functions_framework

from helpers.utils import as_cloud_function

app = FastAPI()


@app.get("/hello_world")
async def get_user_name():
    return {"Hello": "World"}


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
