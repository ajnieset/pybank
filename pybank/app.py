from fastapi import FastAPI
from routers import accounts, users


app = FastAPI()

app.include_router(accounts.router)

@app.get("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    ...