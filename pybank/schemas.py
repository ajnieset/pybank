from typing import Optional
from pydantic import BaseModel


class CreateAccountRequest(BaseModel):
    user_id: int


class AccountBase(BaseModel):
    balance: float
    user_id: int


class UserBase(BaseModel):
    email: str
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class Account(BaseModel):
    id: int
    balance: float
    user_id: int
    User: Optional["User"]


    class Config:
        from_attributes = True
