# main.py
from fastapi import FastAPI
from routes.todo_routes import router

app = FastAPI()
app.include_router(router, prefix="/api/todo", tags=["todos"])