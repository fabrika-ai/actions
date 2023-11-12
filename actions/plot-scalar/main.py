from typing import List, Tuple
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import functions_framework
from fastapi.responses import StreamingResponse

from helpers.utils import as_cloud_function
import matplotlib.pyplot as plt
from io import BytesIO

app = FastAPI()


class GraphData(BaseModel):
    data_points: List[Tuple[str, float]]  # Assuming x_value is a string (like a date) and y_value is a float


def plot_data(data_points):
    x_values, y_values = zip(*data_points)  # Unzipping the list of tuples
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker='o')  # You can customize the plot here
    plt.title("Scalar Data Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer


@app.post("/plot/", response_class=StreamingResponse)
async def plot_graph(graph_data: GraphData):
    if not graph_data.data_points:
        raise HTTPException(status_code=400, detail="No data points provided")

    image = plot_data(graph_data.data_points)
    return StreamingResponse(image, media_type="image/png")


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
