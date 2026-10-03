from datetime import datetime
from pydantic import BaseModel, Field
from domain.types import PermissionType


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

class CreateMessageTargetRequest(BaseModel):
    message_id : int = Field(gt=0)
    destination_id : int = Field(gt=0)
    send_at: datetime
