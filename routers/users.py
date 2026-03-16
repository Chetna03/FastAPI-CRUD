from fastapi import APIRouter
from schemas import User

router = APIRouter()

users = []

@router.post("/users")
def create_user(user: User):
    users.append(user)
    return user

@router.get("/users")
def get_users():
    return users

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]

@router.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    users[user_id] = user
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return users.pop(user_id)