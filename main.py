from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
users = []

class User(BaseModel):
    name: str
    age: int
    email: str

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user

@app.post("/users")
def create_user(user: User):
    return user

@app.get("/search")
def search_users(name: Optional[str] = None):
    return {"searching_for": name}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    users[user_id] = user
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted_user = users.pop(user_id)
    return deleted_user