from typing import Optional
from pydantic import BaseModel


class AccountBase(BaseModel):
    balance: float
    user_id: int
    type: str


class UserBase(BaseModel):
    email: str
    password: str


class User(UserBase):
    id: int
    Account: Optional["AccountBase"]

    class Config:
        from_attributes = True


class Account(AccountBase):
    id: int
    User: UserBase

    class Config:
        from_attributes = True
