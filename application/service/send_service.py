from infrastructure.platforms.senders import *
from domain.entities import MessageTarget, Message, Destination, Media, BotAccount
from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError, InvalidStateError, AppError
from typing import Callable
from domain.types import MessageTargetStatusType


class SendService:

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
        with container.unit_of_work:
            container.logger.log(
                message,
                # f"message with id {id} sent ",
                container.logger.category.SYSTEM,
                container.logger.level.INFO,
                self.send_message.__name__,
            )

    async def send_message(self, message_target: MessageTarget) -> bool:
        message_target.change_status(MessageTargetStatusType.PROCESSING)
        file = None
        data = self.get_send_message_data(message_target)
        if not data["ssucces"]:
            self.error_handler(message_target, data["type"], data["message"])
            return False
        message, bot, media, destination = data["result"]
        send_func = self.proccess_message_data(message, destination)
        if media:
            file = self.get_meida(media.stored_name, media.type.value)

        token = self.get_token(bot.token)
        result = await send_func(
            chat_id=destination.external_id, token=token, text=message.text, file=file
        )
        return result

    def error_handler(self, message_target, error_type, message):
        self._log(message + "error : " + error_type.__class__.__name__)

        message_target.increase_retry_count()
        message_target.save_last_error(f"{error_type} : {message}")
        message_target.change_status(MessageTargetStatusType.FAILED)
        with container.unit_of_work as uow:
            uow.MessageTarget.update(message_target)
        raise error_type(message)

    def get_send_message_data(self, message_target: MessageTarget):
        media = None
        with container.unit_of_work as uow:

            message = uow.Message.get_by_id(message_target.message_id)
            if not message:
                return {
                    "ssucces": False,
                    "type": NotFoundError,
                    "message": "message not found",
                }

            destination = uow.Destination.get_by_id(message_target.destination_id)
            if not destination:
                return {
                    "ssucces": False,
                    "type": NotFoundError,
                    "message": "destination not found",
                }

            if not destination.bot_account_id:
                return {
                    "ssucces": False,
                    "type": InvalidStateError,
                    "message": "destination.bot_account_id is not defined",
                }

            bot = uow.BotAccount.get_by_id(destination.bot_account_id)
            if not bot:
                return {
                    "ssucces": False,
                    "type": NotFoundError,
                    "message": "bot not found",
                }

            if message.media_id:
                media = uow.Media.get_by_id(message.media_id)
                if not media:
                    return {
                        "ssucces": False,
                        "type": NotFoundError,
                        "message": "media not found",
                    }

            return {"ssucces": True, "result": [message, bot, media, destination]}

    def proccess_message_data(
        self, message: Message, destination: Destination
    ) -> Callable:
        platform = destination.platform
        sender = self.senders[platform.value]
        func = self.message_type[message.type.value]
        return getattr(sender, func)

    def get_meida(self, storage_name: str, media_type) -> bytes:
        return container.storage_service.read_media(storage_name, media_type)

    def get_token(self, token):
        return container.encryption_service.decrip(token)
