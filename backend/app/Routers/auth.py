from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Fake in-memory user store (replace with database later)
fake_users = {
    "admin@ledgero.com": {
        "password": "123456"
    }
}

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    user = fake_users.get(data.email)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "message": "Login successful",
        "user": data.email
    }
