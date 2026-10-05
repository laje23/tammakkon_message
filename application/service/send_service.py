from infrastructure.platforms.senders import *
from domain.entities import MessageTarget, Message, Destination, Media, BotAccount
from domain.exeptions import NotFoundError, InvalidStateError, AppError
from typing import Callable
from domain.types import MessageTargetStatusType
from application.service import EncryptionService, LogService, StorageService
from infrastructure.database.unit_of_work import UnitOfWork


class SendService:
    uow = UnitOfWork()
    logger = LogService(uow)
    storage_service = StorageService()
    encription = EncryptionService()

    message_type = {
        "text": "send_text",
        "photo": "send_photo",
        "audio": "send_audio",
        "video": "send_video",
        "document": "send_document",
    }

    senders = {
        "bale": BaleSender,
        "eitaa": EitaaSender,
        "robika": RobikaSender,
    }

    def __init__(self) -> None: ...

    def _log(self, message: str):

        with self.uow:
            self.logger.log(
                message,
                self.logger.category.SYSTEM,
                self.logger.level.INFO,
                self.send_message.__name__,
            )

    async def send_message(self, message_target) -> bool:


        # -----------------------------------------
        # Get send data
        # -----------------------------------------


        data = self.get_send_message_data(message_target)


        if not data["success"]:


            self.error_handler(
                message_target,
                data["type"],
                data["message"],
            )

            return False


        # -----------------------------------------
        # Extract data
        # -----------------------------------------

        message = data["message"]
        destination = data["destination"]
        bot = data["bot"]
        media = data["media"]


        send_func = self.proccess_message_data(
            message,
            destination,
        )

        # -----------------------------------------
        # Get media
        # -----------------------------------------

        file = None

        if media:

            file = self.get_meida(
                media.stored_name,
                media.type.value,
            )



        # -----------------------------------------
        # Get token
        # -----------------------------------------


        token = self.get_token(bot.token)


        # -----------------------------------------
        # Send message
        # -----------------------------------------
        result = send_func(
            chat_id=destination.external_id,
            token=token,
            text=message.text,
            file=file,
        )
        # -----------------------------------------
        # Send result
        # -----------------------------------------


        return result

    def error_handler(
        self,
        message_target: MessageTarget,
        error_type,
        message: str,
    ):

        print(
            f"ERROR HANDLER | " f"type={error_type.__name__} | " f"message={message}",
            flush=True,
        )

        self._log(message + " error : " + error_type.__name__)

        print("ERROR HANDLER - increase_retry_count", flush=True)

        message_target.increase_retry_count()

        print("ERROR HANDLER - save_last_error", flush=True)

        message_target.save_last_error(f"{error_type.__name__}: {message}")

        print("ERROR HANDLER - change_status", flush=True)

        message_target.change_status(MessageTargetStatusType.FAILED)

        print("ERROR HANDLER - update DB START", flush=True)

        with self.uow as uow:
            uow.MessageTarget.update(message_target)

        print("ERROR HANDLER - update DB DONE", flush=True)

        raise error_type(message)

    def get_send_message_data(self, message_target):

        print(
            "GET DATA - message_target:",
            message_target,
            flush=True,
        )

        # -----------------------------------------
        # Message
        # -----------------------------------------

        print(
            "GET DATA - getting message",
            flush=True,
        )

        message = message_target.message

        print(
            "GET DATA - message:",
            message,
            flush=True,
        )

        if not message:

            print(
                "GET DATA - message NOT FOUND",
                flush=True,
            )

            return {
                "success": False,
                "type": NotFoundError,
                "message": "message not found",
            }

        # -----------------------------------------
        # Destination
        # -----------------------------------------

        print(
            "GET DATA - getting destination",
            flush=True,
        )

        destination = message_target.destination

        print(
            "GET DATA - destination:",
            destination,
            flush=True,
        )

        if not destination:

            print(
                "GET DATA - destination NOT FOUND",
                flush=True,
            )

            return {
                "success": False,
                "type": NotFoundError,
                "message": "destination not found",
            }

        # -----------------------------------------
        # Bot account id
        # -----------------------------------------

        print(
            "GET DATA - checking bot_account_id",
            flush=True,
        )

        if not destination.bot_account_id:

            print(
                "GET DATA - bot_account_id NOT DEFINED",
                flush=True,
            )

            return {
                "success": False,
                "type": InvalidStateError,
                "message": "destination.bot_account_id is not defined",
            }

        # -----------------------------------------
        # Bot
        # -----------------------------------------

        print(
            "GET DATA - getting bot",
            flush=True,
        )

        bot = destination.bot_account

        print(
            "GET DATA - bot:",
            bot,
            flush=True,
        )

        if not bot:

            print(
                "GET DATA - bot NOT FOUND",
                flush=True,
            )

            return {
                "success": False,
                "type": NotFoundError,
                "message": "bot not found",
            }

        # -----------------------------------------
        # Media
        # -----------------------------------------

        print(
            "GET DATA - getting media",
            flush=True,
        )

        media = message.media

        print(
            "GET DATA - media:",
            media,
            flush=True,
        )

        if message.media_id and not media:

            print(
                "GET DATA - media NOT FOUND",
                flush=True,
            )

            return {
                "success": False,
                "type": NotFoundError,
                "message": "media not found",
            }

        # -----------------------------------------
        # Success
        # -----------------------------------------

        print(
            "GET DATA - SUCCESS",
            flush=True,
        )

        return {
            "success": True,
            "message": message,
            "destination": destination,
            "bot": bot,
            "media": media,
        }

    def proccess_message_data(
        self,
        message: Message,
        destination: Destination,
    ) -> Callable:

        print(
            "PROCESS DATA - platform:",
            destination.platform,
            flush=True,
        )

        platform = destination.platform

        print(
            "PROCESS DATA - platform value:",
            platform.value,
            flush=True,
        )

        sender = self.senders[platform.value]()

        print(
            "PROCESS DATA - sender:",
            sender,
            flush=True,
        )

        print(
            "PROCESS DATA - message type:",
            message.type,
            flush=True,
        )

        print(
            "PROCESS DATA - message type value:",
            message.type.value,
            flush=True,
        )

        func = self.message_type[message.type.value]

        print(
            "PROCESS DATA - function name:",
            func,
            flush=True,
        )

        send_function = getattr(
            sender,
            func,
        )

        print(
            "PROCESS DATA - function:",
            send_function,
            flush=True,
        )

        return send_function

    def get_meida(
        self,
        storage_name: str,
        media_type,
    ) -> bytes:

        print(
            "GET MEDIA - START",
            flush=True,
        )

        print(
            f"GET MEDIA - storage_name={storage_name}",
            flush=True,
        )

        print(
            f"GET MEDIA - media_type={media_type}",
            flush=True,
        )

        result = self.storage_service.read_media(
            storage_name,
            media_type,
        )

        print(
            f"GET MEDIA - DONE | size={len(result)} bytes",
            flush=True,
        )

        return result

    def get_token(self, token):

        print("GET TOKEN - START", flush=True)

        result = self.encription.decrip(token)

        print("GET TOKEN - DONE", flush=True)

        return result
