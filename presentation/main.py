from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from presentation.controllers import *


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

class UpdateBotRequest(BaseModel):
    name: str
    platform: str
    is_active: bool
    token: str | None = None
    
class UpdateDestinationRequest(BaseModel):
    name: str
    platform: str
    is_active: bool
    external_id : str 
    bot_account_id : str
    type : str 
    
    
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
    data = DashboardController().get_datas()

    return data


@app.get("/bot")
async def get_bots():
    return BotAccountController().get_all_bots()


@app.get("/bot/{id}")
async def get_bot(id: int):
    return BotAccountController().get_bot_account_by_id(id)

    
@app.put("/bot/{id}")
async def update_bot(
    id: int,
    data: UpdateBotRequest
):
    return BotAccountController().update_bot_account(id, data)


@app.get("/destination")
async def get_destinations():
    return DestinationController().get_all_destinations()


@app.get("/destination/{id}")
async def get_destination(id: int):
    return DestinationController().get_destination_by_id(id)

    
@app.put("/destination/{id}")
async def update_destination(
    id: int,
    data: UpdateBotRequest
):
    return DestinationController().update_destination(id, data)
