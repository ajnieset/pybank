from typing import Optional
from pydantic import BaseModel


class CreateAccountRequest(BaseModel):
    user_id: int

class AccountBase(BaseModel):
    balance: float
    user_id: int
    User: Optional[User] = None


class Account(AccountBase):
    id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str
    password: str

    
class User(UserBase):
    id: int

    class Config:
        from_attributes = True