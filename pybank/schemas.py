from typing import Optional
from pydantic import BaseModel


class AccountBase(BaseModel):
    balance: float
    user_id: int
    User: Optional[User] = None


class Account(AccountBase):
    id: int

    class Config:
        from_attributes = True

class User(BaseModel):
    ...