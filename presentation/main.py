from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from presentation.controllers import authenticate 


app = FastAPI()


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Schemas
# =========================

class LoginRequest(BaseModel):
    username: str
    password: str


# =========================
# Routes
# =========================

@app.get("/")
async def root():
    return {
        "message": "Backend is running"
    }


@app.post("/login")
async def login(data: LoginRequest):
    return authenticate(data)


# =========================
# Dashboard
# =========================

import json
from pathlib import Path


@app.get("/dashboard")
async def dashboard():

    path = Path("dashboard_test.json")

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data