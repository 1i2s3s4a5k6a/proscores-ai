from fastapi import APIRouter, HTTPException
import jwt, os

router = APIRouter()
SECRET = os.getenv("JWT_SECRET")

def create_token(user_id):
    return jwt.encode({"uid": user_id}, SECRET, algorithm="HS256")

@router.post("/login")
def login(email: str):
    return {"access_token": create_token(email)}
