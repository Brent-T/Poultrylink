from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID, uuid4
from app.models.shared import RoleEnum


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    phone: str
    location: str
    role: RoleEnum


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: str
    role: RoleEnum
    full_name: str
    
    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
