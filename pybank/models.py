from __future__ import annotations
from typing import Annotated, Any
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

from .schemas import Account as AccountData, UserBase, User as UserData


class Base(DeclarativeBase):
    ...


# Annotated types
intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
user_fk = Annotated[int, mapped_column(ForeignKey("users.id"))]


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[intpk]
    balance: Mapped[float]
    user_id: Mapped[user_fk]
    user: Mapped["User"] = relationship(back_populates="account")

    @classmethod
    def get_by_id(cls, id: int, db: Session) -> Account:
        return db.query(cls).filter_by(id=id).first()

    @classmethod
    def create_account(cls, data: AccountData, db: Session):
        db.add(cls(balance=0.00, user_id=data.user_id))
        db.commit()


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    account: Mapped["Account"] = relationship(back_populates="user")

    @classmethod
    def get_by_id(cls, id: int, db: Session) -> User:
        return db.query(cls).filter_by(id=id).first()

    @classmethod
    def create_user(cls, data: UserBase, db: Session):
        db.add(cls(email=data.email, password=data.password))
        db.commit()

    @classmethod
    def update_user(cls, data: UserBase, db: Session):
        ...

    @classmethod
    def delete_user(cls, user_id: int, db: Session):
        user_to_delete = User.get_by_id(user_id, db)
        db.delete(user_to_delete)
        db.commit()
