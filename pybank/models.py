from typing import Annotated, Any
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

from .schemas import Account as AccountData, User as UserData


class Base(DeclarativeBase):
    ...


# Annotated types
intpk = Annotated[int, mapped_column(primary_key=True)]
# user_fk = Annotated[int, mapped_column(ForeignKey("users.id"))]


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[intpk]
    balance: Mapped[float]
    user_id: Mapped[int]
    # user: Mapped["Account"] = relationship("User", back_populates="account")

    def __init__(self, id: int, balance: float, user_id: int, user: UserData = None):
        self.id = id
        self.balance = balance
        self.user_id = user_id
        # self.user = user

    @classmethod
    def get_by_id(cls, id: int, db: Session):
        return db.query(cls).filter_by(id=id).first()
    
    @classmethod
    def create_account(cls, data: AccountData, db: Session):
        db.add(cls(id=data.id, balance=data.balance, user_id=data.user_id, user=None))
        db.commit()


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    # account: Mapped["User"] = relationship("Account", back_populates="user")

    @classmethod
    def get_by_id(cls, id: int, db: Session):
        return db.query(cls).filter_by(id=id).first()
