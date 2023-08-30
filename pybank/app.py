from fastapi import FastAPI
from .routers import accounts, users
from . import models
from .db import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(accounts.router)
app.include_router(users.router)


@app.get("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    ...
