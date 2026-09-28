from fastapi import UploadFile
from domain.exeptions import NotFoundError
from infrastructure.dependency_Injection import container
from domain.entities import Message, Media
import mimetypes
from fastapi.responses import Response
from presentation.controllers.decorators import safe_class


@safe_class
class MessageController:

    container = container

    def _log(self, message):
        self.container.logger.log(
            message,
            self.container.logger.category.SYSTEM,
            self.container.logger.level.INFO,
            self.__class__.__name__,
        )

    async def create_message(
        self,
        message_type: str,
        text: str,
        file: UploadFile | None,
    ):
        media_id = None

        if file is not None:
            media_file = await file.read()

            media_name = file.filename
            media_size = len(media_file)
            storage_name = file.filename

            media_id = self.create_media(
                name=media_name,  # type: ignore
                storage_name=storage_name,  # type: ignore
                media_file=media_file,
                size=media_size,
            )

        message = Message(
            None,
            media_id,
            message_type.upper(),  # type: ignore
            text,
            created_by=1,
        )

        with self.container.unit_of_work as uow:
            uow.Message.create(message)
        self._log("message created")

        return {"success": True, "message": "پیام با موفقیت ثبت شد"}

    def create_media(
        self,
        name: str,
        storage_name: str,
        media_file: bytes,
        size: int,
    ):
        storage_name = "storage/" + storage_name
        self.container.media_service.save_media(storage_name, media_file)

        media = Media(None, name, storage_name, size)

        with self.container.unit_of_work as uow:
            media_id = uow.Media.create(media)

        self._log("media created")
        return media_id

    def get_messages(self, page: int = 1, page_size: int = 12):
        with self.container.unit_of_work as uow:

            messages = uow.Message.get_paginated(page=page, page_size=page_size)

            total = uow.Message.get_totel_count()

        total_pages = (total + page_size - 1) // page_size

        return {
            "items": messages,
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_previous": page > 1,
        }

    def get_message_by_id(self, id):
        with self.container.unit_of_work as uow:
            message = uow.Message.get_by_id(id)

            if not message:
                raise NotFoundError("message not found")

            media = None

            if message.media_id:
                media = uow.Media.get_by_id(message.media_id)

                if not media:
                    raise NotFoundError("media not found")

            return {"message": message, "media": media}

    def get_media(self, id: int):
        with self.container.unit_of_work as uow:
            media = uow.Media.get_by_id(id)

            if not media:
                raise NotFoundError("media not found")

            media_file = self.container.media_service.read_media(media.stored_name)

            media_type, _ = mimetypes.guess_type(media.stored_name)

            return Response(
                content=media_file, media_type=media_type or "application/octet-stream"
            )

    def delete_message(self, id: int):
        with self.container.unit_of_work as uow:
            message = uow.Message.get_by_id(id)

            if not message:
                raise NotFoundError("message not found")
            if message.id:
                if uow.MessageTarget.exist_by_message_id(message.id):
                    return {"success": False, "message": "پیام زمانبندی شده است"}

            uow.Message.delete(id)

        self._log("message deleted")
        return {"success": True, "message": "پیام با موفقیت حذف شد"}

    def update_message(self, id: int, text: str):
        with self.container.unit_of_work as uow:
            message = uow.Message.get_by_id(id)

            if not message:
                raise NotFoundError("message not found")

            message.update(text=text)

            uow.Message.update(message)

        self._log("message updated")
        return {"success": True, "message": "پیام با موفقیت ویرایش شد"}
