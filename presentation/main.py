from fastapi import FastAPI , Query , File, Form, UploadFile 
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
    bot_account_id : int
    type : str 
    

class CreateBotRequest(BaseModel):
    name: str
    platform: str
    is_active: bool
    token: str


class CreateDestinationRequest(BaseModel):
    name: str
    platform: str
    is_active: bool
    external_id: str
    bot_account_id: int | None
    type: str



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


@app.post("/bot")
async def create_bot(data: CreateBotRequest):
    return BotAccountController().create_bot_account(data)


@app.put("/bot/{id}")
async def update_bot(
    id: int,
    data: UpdateBotRequest
):
    return BotAccountController().update_bot_account(id, data)


@app.delete("/bot/{id}")
async def delete_bot(id: int):
    return BotAccountController().delete_bot_account(id)

@app.get("/destination")
async def get_destinations():
    return DestinationController().get_all_destinations()


@app.get("/destination/{id}")
async def get_destination(id: int):
    return DestinationController().get_destination_by_id(id)


@app.post("/destination")
async def create_destination(data: CreateDestinationRequest):
    return DestinationController().create_destination(data)


@app.put("/destination/{id}")
async def update_destination(
    id: int,
    data: UpdateDestinationRequest
):
    return DestinationController().update_destination(id, data)


@app.delete("/destination/{id}")
async def delete_destination(id: int):
    return DestinationController().delete_destination(id)

from fastapi import Query

@app.get("/message")
async def get_messages(
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=100)
):
    return MessageController().get_messages(
        page=page,
        page_size=page_size
    )

@app.post("/message")
async def create_message(
    message_type: str = Form(...),
    text: str = Form(""),
    file: UploadFile | None = File(None),
):
    return await MessageController().create_message(
        message_type=message_type,
        text=text,
        file=file,
    )
    
@app.get("/message/{id}")
async def get_message(id:int):
    return MessageController().get_message_by_id(id)


@app.get("/media/{id}")
async def get_media(id: int):
    return MessageController().get_media(id)