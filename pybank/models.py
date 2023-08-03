from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    ...


class Account(Base):
    __tablename__ = "accounts"

    id = mapped_column()

    user = relationship("User", back_populates="account")


class User(Base):
    __tablename__ = "users"

    id = mapped_column()

    account = relationship("Account", back_populates="user")
