from fastapi import FastAPI, Query, File, Form, UploadFile
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
    external_id: str
    bot_account_id: int | None = None
    type: str


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


class CreateUserRequest(BaseModel):
    user_name: str
    password: str
    is_active: bool = True


class UpdateUserRequest(BaseModel):
    user_name: str
    password: str | None = None
    is_active: bool


class UpdateUserRolesRequest(BaseModel):
    remove_list: list[int] = []
    add_list: list[int] = []


class UpdatePlatformSettingRequest(BaseModel):
    limit_character: int | None = None
    limit_file_size: int | None = None
    bale_base_url: str | None = None
    bale_active: bool | None = None
    eitaa_base_url: str | None = None
    eitaa_active: bool | None = None
    robika_base_url: str | None = None
    robika_active: bool | None = None


class UpdateSenderSettingRequest(BaseModel):
    time_out: int | None = None
    max_try: int | None = None
    use_poroxy: bool | None = None


# =========================
# Routes
# =========================


@app.get("/")
async def root():
    return {"message": "Backend is running"}


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
async def update_bot(id: int, data: UpdateBotRequest):
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
async def update_destination(id: int, data: UpdateDestinationRequest):
    return DestinationController().update_destination(id, data)


@app.delete("/destination/{id}")
async def delete_destination(id: int):
    return DestinationController().delete_destination(id)


from fastapi import Query


@app.get("/message")
async def get_messages(
    page: int = Query(1, ge=1), page_size: int = Query(12, ge=1, le=100)
):
    return MessageController().get_messages(page=page, page_size=page_size)


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
async def get_message(id: int):
    return MessageController().get_message_by_id(id)


@app.get("/media/{id}")
async def get_media(id: int):
    return MessageController().get_media(id)


@app.delete("/message/{id}")
async def delete_message(id: int):
    return MessageController().delete_message(id)


@app.put("/message/{id}")
async def update_message(id: int, text: str = Form("")):
    return MessageController().update_message(id=id, text=text)


# =========================
# Users
# =========================


@app.get("/user")
async def get_users():
    return UserController().get_all_user()


@app.get("/user/{id}")
async def get_user(id: int):
    return UserController().get_user_by_id(id)


@app.post("/user")
async def create_user(data: CreateUserRequest):
    return UserController().create_user(data)


@app.put("/user/{id}")
async def update_user(id: int, data: UpdateUserRequest):
    return UserController().update_user(id=id, data=data)


@app.delete("/user/{id}")
async def delete_user(id: int):
    return UserController().delete_user(id)


@app.get("/user/{id}/roles")
async def get_user_roles(id: int):
    return UserController().get_roles(id)


@app.put("/user/{id}/roles")
async def update_user_roles(id: int, data: UpdateUserRolesRequest):
    return UserController().update_roles(id, data)


@app.get("/settings/logs")
async def get_logs():
    return LogController().get_logs()


@app.get("/settings/platforms")
async def get_platform_setting():
    return PlatformSettingController().get_setting()


@app.put("/settings/platforms")
async def update_platform_setting(data: UpdatePlatformSettingRequest):
    return PlatformSettingController().update_setting(data)


@app.get("/settings/sends")
async def get_sender_setting():
    return SenderSettingController().get_setting()


@app.put("/settings/sends")
async def update_sender_setting(data: UpdateSenderSettingRequest):
    return SenderSettingController().update_setting(data)
