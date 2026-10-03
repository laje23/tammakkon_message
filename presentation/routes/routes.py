from presentation.schames import *
from presentation.controllers import *
from fastapi import (
    Query,
    File,
    Form,
    UploadFile,
)
from fastapi import (
    FastAPI,
)


class Ruotes:
    def __init__(self, app: FastAPI):
        self.app = app

    def defination_routes(self):

        # =========================
        # Public Routes
        # =========================

        @self.app.get("/")
        async def root():
            return {"message": "Backend is running"}

        @self.app.post("/login")
        async def login(data: LoginRequest):
            return authenticate(data)

        # =========================
        # Dashboard
        # =========================

        @self.app.get("/dashboard")
        async def dashboard():
            return DashboardController().get_datas()

        # =========================
        # Bot
        # =========================

        @self.app.get("/bot")
        async def get_bots():
            return BotAccountController().get_all_bots()

        @self.app.get("/bot/{id}")
        async def get_bot(id: int):
            return BotAccountController().get_bot_account_by_id(id)

        @self.app.post("/bot")
        async def create_bot(data: CreateBotRequest):
            return BotAccountController().create_bot_account(data)

        @self.app.put("/bot/{id}")
        async def update_bot(
            id: int,
            data: UpdateBotRequest,
        ):
            return BotAccountController().update_bot_account(
                id,
                data,
            )

        @self.app.delete("/bot/{id}")
        async def delete_bot(id: int):
            return BotAccountController().delete_bot_account(id)

        # =========================
        # Destination
        # =========================

        @self.app.get("/destination")
        async def get_destinations():
            return DestinationController().get_all_destinations()

        @self.app.get("/destination/{id}")
        async def get_destination(id: int):
            return DestinationController().get_destination_by_id(id)

        @self.app.post("/destination")
        async def create_destination(
            data: CreateDestinationRequest,
        ):
            return DestinationController().create_destination(data)

        @self.app.put("/destination/{id}")
        async def update_destination(
            id: int,
            data: UpdateDestinationRequest,
        ):
            return DestinationController().update_destination(
                id,
                data,
            )

        @self.app.delete("/destination/{id}")
        async def delete_destination(id: int):
            return DestinationController().delete_destination(id)

        # =========================
        # Message
        # =========================

        @self.app.get("/message")
        async def get_messages(
            page: int = Query(1, ge=1),
            page_size: int = Query(12, ge=1, le=100),
        ):
            return MessageController().get_messages(
                page=page,
                page_size=page_size,
            )

        @self.app.post("/message")
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

        @self.app.get("/message/{id}")
        async def get_message(id: int):
            return MessageController().get_message_by_id(id)

        @self.app.get("/media/{id}")
        async def get_media(id: int):
            return MessageController().get_media(id)

        @self.app.delete("/message/{id}")
        async def delete_message(id: int):
            return MessageController().delete_message(id)

        @self.app.put("/message/{id}")
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

        @self.app.get("/user")
        async def get_users():
            return UserController().get_all_user()

        @self.app.get("/user/{id}")
        async def get_user(id: int):
            return UserController().get_user_by_id(id)

        @self.app.post("/user")
        async def create_user(
            data: CreateUserRequest,
        ):
            return UserController().create_user(data)

        @self.app.put("/user/{id}")
        async def update_user(
            id: int,
            data: UpdateUserRequest,
        ):
            return UserController().update_user(
                id=id,
                data=data,
            )

        @self.app.delete("/user/{id}")
        async def delete_user(id: int):
            return UserController().delete_user(id)

        @self.app.get("/user/{id}/roles")
        async def get_user_roles(id: int):
            return UserController().get_roles(id)

        @self.app.put("/user/{id}/roles")
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

        @self.app.get("/settings/logs")
        async def get_logs():
            return LogController().get_logs()

        @self.app.get("/settings/platforms")
        async def get_platform_setting():
            return PlatformSettingController().get_setting()

        @self.app.put("/settings/platforms")
        async def update_platform_setting(
            data: UpdatePlatformSettingRequest,
        ):
            return PlatformSettingController().update_setting(data)

        @self.app.get("/settings/sends")
        async def get_sender_setting():
            return SenderSettingController().get_setting()

        @self.app.put("/settings/sends")
        async def update_sender_setting(
            data: UpdateSenderSettingRequest,
        ):
            return SenderSettingController().update_setting(data)

        @self.app.get("/settings/storage")
        async def get_storage_setting():
            return StorageSettingController().get_storage_setting()

        @self.app.put("/settings/storage")
        async def update_storege_setting(
            data: UpdateStorageSettingRequest,
        ):
            return StorageSettingController().update_setting(data)

        @self.app.put("/settings/roles/{id}")
        async def update_role(
            id: int,
            data: UpdateRoleRequest,
        ):
            return RoleController().update_role(id, data)

        @self.app.delete("/settings/roles/{id}")
        async def delete_role(
            id: int,
        ):
            return RoleController().delete_role(id)

        @self.app.post("/settings/roles")
        async def create_role(
            data: CreateRoleRequest,
        ):
            return RoleController().create_role(data)

        @self.app.get("/settings/roles")
        async def get_roles():
            return RoleController().get_roles()

        @self.app.get("/settings/roles/{id}/permissions")
        async def get_role_permissions(id: int):
            return RoleController().get_role_permissions(id)

        @self.app.put("/settings/roles/{id}/permissions")
        async def update_role_permissions(id: int, data: UpdateRolePermissionRequest):
            return RoleController().update_role_permissions(id, data)

        @self.app.get("/settings/roles/{id}")
        async def get_role(id: int):
            return RoleController().get_role_by_id(id)

        @self.app.get("/auth/permissions/{id}")
        async def get_user_permission(id: int):
            return UserController().get_user_permissions(id)

        @self.app.get("/message_target")
        async def get_message_targets():
            return MessageTargetController().get_all_message_target()

        @self.app.get("/message_target/{id}")
        async def get_message_target(id: int):
            return MessageTargetController().get_message_target_by_id(id)

        @self.app.post("/message_target")
        async def create_message_target(data: CreateMessageTargetRequest):
            return MessageTargetController().create_message_target(data)

        @self.app.put("/message_target/{id}/cancel")
        async def cancel_message_target(id: int):
            return MessageTargetController().cancel_message_target(id)

        @self.app.put("/message_target/{id}/resume")
        async def resume_message_target(id: int):
            return MessageTargetController().resume_message_target(id)

        @self.app.delete("/message_target/{id}")
        async def delete_message_target(id: int):
            return MessageTargetController().delete_message_target(id)
