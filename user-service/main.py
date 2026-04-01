from fastapi import FastAPI
from models import User
from service import fetch_users, add_user

app = FastAPI(title="User Service")

@app.get("/api/users")
def get_users():
    return fetch_users()

@app.post("/api/users")
def create_user(user: User):
    return add_user(user)