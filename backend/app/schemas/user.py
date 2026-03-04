from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr = Field(..., description="Email пользователя")
    username: str = Field(..., min_length=3, max_length=50, description="Имя пользователя")


class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Пароль (минимум 6 символов)")


class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="Email пользователя")
    password: str = Field(..., description="Пароль")


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class TokenData(BaseModel):
    user_id: Optional[int] = None
    email: Optional[str] = None
