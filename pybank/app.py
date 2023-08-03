from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    ...