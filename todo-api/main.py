from fastapi import FastAPI
from routes import todo

app: FastAPI = FastAPI()

app.include_router(todo.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}