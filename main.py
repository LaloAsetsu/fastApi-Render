from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    first: float
    second: float

class User(BaseModel):
    username: str
    password: str

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/sum")
async def sum(item: Item):
    return {"result": item.first + item.second}

@app.post("/subtract")
async def subtract(item: Item):
    return {"result": item.first - item.second}

@app.post("/multiply")
async def multiply(item: Item):
    return {"result": item.first * item.second}

@app.post("/divide")
async def divide(item: Item):
    if item.second == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": item.first / item.second}

@app.post("/login")
async def login(user: User):
    if user.username == "admin" and user.password == "password":
        return {"result": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
