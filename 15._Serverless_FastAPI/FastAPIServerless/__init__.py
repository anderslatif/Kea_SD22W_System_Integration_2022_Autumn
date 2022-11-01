import azure.functions as func
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}."}

@app.get("/greet/{name}/age/{age}")
def greet(name: str, age: int):
    return {"message": f"Hello {name}. You are {age} years old."}

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)
