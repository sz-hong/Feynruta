from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field
from .tokens import issue_token, revoke
from typing import Annotated
from .deps import get_current_user

class RegisterRequest(BaseModel):
    username: str
    password: str = Field(min_length=8)

class LoginRequest(BaseModel):
    username: str
    password: str

users: dict[str, str] = {}

router = APIRouter()

@router.post("/login")
async def login(body: LoginRequest):
    if body.username not in users or body.password != users[body.username]:
        raise HTTPException(
            status_code=401,
            detail="BAD_CREDENTIALS"
        )
    token = await issue_token(body.username)
    return {"token": token, "user": {"username": body.username}}

@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(username: Annotated[str, Depends(get_current_user)]):
    await revoke(username)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: RegisterRequest):
    if body.username in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail = "USERNAME_TAKEN",
        )
    users[body.username] = body.password
    return {"username": body.username}
        