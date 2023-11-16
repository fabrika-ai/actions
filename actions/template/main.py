import os

from openai import OpenAI

from fastapi import FastAPI
import functions_framework

from helpers.utils import as_cloud_function

app = FastAPI()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY") or None
)


@app.get("/hello-world")
async def get_user_name():
    return {"Hello": "World"}


@app.post("/question-answering")
async def generate_completion(question: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return {
        "answer": completion.choices[0].message
    }


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
