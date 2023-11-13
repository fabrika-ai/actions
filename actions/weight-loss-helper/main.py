from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import functions_framework

from helpers.utils import as_cloud_function

app = FastAPI()

# Global data storage
calory_helper = {'datetime': [], 'calories': []}

# Pydantic model to parse incoming data
class CalorieRecord(BaseModel):
    datetime: str
    calories: int

@app.post("/store_record")
async def store_record(new_calorie_record: CalorieRecord):
    # Logic to process and store the new record
    calory_helper['datetime'].append(new_calorie_record.datetime)
    calory_helper['calories'].append(new_calorie_record.calories)
    return {"message": "Record stored successfully"}

@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
