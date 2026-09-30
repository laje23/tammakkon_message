from fastapi import (
    FastAPI,
    Query,
    File,
    Form,
    UploadFile,
)

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from presentation.controllers import *
from domain.types import PermissionType

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
    bot_account_id: int | None = None
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
    remove_list: list[int] = Field(default_factory=list)
    add_list: list[int] = Field(default_factory=list)


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


class UpdateStorageSettingRequest(BaseModel):
    photo: str | None = None
    audio: str | None = None
    video: str | None = None
    document: str | None = None
    storage_capacity_mb: int | None = None

class UpdateRoleRequest(BaseModel):
    name: str | None = None
    description: str | None = None


class CreateRoleRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = None


class UpdateRolePermissionRequest(BaseModel):
    add_list: list[PermissionType] = Field(default_factory=list)
    remove_list: list[PermissionType] = Field(default_factory=list)

# =========================
# Public Routes
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

@app.get("/dashboard")
async def dashboard():
    return DashboardController().get_datas()


# =========================
# Bot
# =========================

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
    data: UpdateBotRequest,
):
    return BotAccountController().update_bot_account(
        id,
        data,
    )


@app.delete("/bot/{id}")
async def delete_bot(id: int):
    return BotAccountController().delete_bot_account(id)


# =========================
# Destination
# =========================

@app.get("/destination")
async def get_destinations():
    return DestinationController().get_all_destinations()


@app.get("/destination/{id}")
async def get_destination(id: int):
    return DestinationController().get_destination_by_id(id)


@app.post("/destination")
async def create_destination(
    data: CreateDestinationRequest,
):
    return DestinationController().create_destination(data)


@app.put("/destination/{id}")
async def update_destination(
    id: int,
    data: UpdateDestinationRequest,
):
    return DestinationController().update_destination(
        id,
        data,
    )


@app.delete("/destination/{id}")
async def delete_destination(id: int):
    return DestinationController().delete_destination(id)


# =========================
# Message
# =========================

@app.get("/message")
async def get_messages(
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=100),
):
    return MessageController().get_messages(
        page=page,
        page_size=page_size,
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
async def get_message(id: int):
    return MessageController().get_message_by_id(id)


@app.get("/media/{id}")
async def get_media(id: int):
    return MessageController().get_media(id)


@app.delete("/message/{id}")
async def delete_message(id: int):
    return MessageController().delete_message(id)


@app.put("/message/{id}")
async def update_message(
    id: int,
    text: str = Form(""),
):
    return MessageController().update_message(
        id=id,
        text=text,
    )


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
async def create_user(
    data: CreateUserRequest,
):
    return UserController().create_user(data)


@app.put("/user/{id}")
async def update_user(
    id: int,
    data: UpdateUserRequest,
):
    return UserController().update_user(
        id=id,
        data=data,
    )


@app.delete("/user/{id}")
async def delete_user(id: int):
    return UserController().delete_user(id)


@app.get("/user/{id}/roles")
async def get_user_roles(id: int):
    return UserController().get_roles(id)


@app.put("/user/{id}/roles")
async def update_user_roles(
    id: int,
    data: UpdateUserRolesRequest,
):
    return UserController().update_roles(
        id,
        data,
    )


# =========================
# Settings
# =========================

@app.get("/settings/logs")
async def get_logs():
    return LogController().get_logs()


@app.get("/settings/platforms")
async def get_platform_setting():
    return PlatformSettingController().get_setting()


@app.put("/settings/platforms")
async def update_platform_setting(
    data: UpdatePlatformSettingRequest,
):
    return PlatformSettingController().update_setting(data)


@app.get("/settings/sends")
async def get_sender_setting():
    return SenderSettingController().get_setting()


@app.put("/settings/sends")
async def update_sender_setting(
    data: UpdateSenderSettingRequest,
):
    return SenderSettingController().update_setting(data)


@app.get("/settings/storage")
async def get_storage_setting():
    return StorageSettingController().get_storage_setting()


@app.put("/settings/storage")
async def update_storege_setting(
    data: UpdateStorageSettingRequest,
):
    return StorageSettingController().update_setting(data)


@app.put("/settings/roles/{id}")
async def update_role(
    id :int ,
    data: UpdateRoleRequest,
):
    return RoleController().update_role(id , data)

@app.delete("/settings/roles/{id}")
async def delete_role(
    id :int ,
):
    return RoleController().delete_role(id)

@app.post("/settings/roles")
async def create_role(
    data: CreateRoleRequest,
):
    return RoleController().create_role(data)

@app.get("/settings/roles")
async def get_roles(
):
    return RoleController().get_roles()

@app.get("/settings/roles/{id}/permissions")
async def get_role_permissions(
    id:int 
):
    return RoleController().get_role_permissions(id)

@app.put("/settings/roles/{id}/permissions")
async def update_role_permissions(
    id:int,
    data : UpdateRolePermissionRequest
):
    return RoleController().update_role_permissions(id , data)

@app.get("/settings/roles/{id}")
async def get_role(id: int):
    return RoleController().get_role_by_id(id)

@app.get("/auth/permissions/{id}")
async def get_user_permission(id: int):
    return UserController().get_user_permissions(id)