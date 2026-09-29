from fastapi import UploadFile
from fastapi.responses import Response

from domain.exeptions import NotFoundError
from domain.entities import Message, Media
from domain.types import MediaType
from infrastructure.dependency_Injection import container
from presentation.controllers.decorators import safe_class

import mimetypes


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

            media_id = self.create_media(
                original_name=file.filename,  # type: ignore
                _media_type=message_type,
                media_file=media_file,
                size=len(media_file),
            )

        message = Message(
            None,
            media_id,
            message_type.upper(),  # type: ignore
            text,
            created_by=1,
        )

        with self.container.unit_of_work as uow:
            self._log("message created")
            uow.Message.create(message)


        return {
            "success": True,
            "message": "پیام با موفقیت ثبت شد",
        }

    def create_media(
        self,
        original_name: str,
        _media_type: str,
        media_file: bytes,
        size: int,
    ):
        with self.container.unit_of_work as uow:
            media_type = MediaType(_media_type.lower())

            stored_name = self.container.storage_service.save_media(
                media_file=media_file,
                media_type=media_type,
                storage_name=original_name,
            )

            media = Media(
                id=None,
                original_name=original_name,
                stored_name=stored_name,
                media_type=media_type,
                size=size,
            )

            media_id = uow.Media.create(media)

            self._log("media created")

        return media_id

    def get_messages(
        self,
        page: int = 1,
        page_size: int = 12,
    ):
        with self.container.unit_of_work as uow:

            messages = uow.Message.get_paginated(
                page=page,
                page_size=page_size,
            )

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

    def get_message_by_id(self, id: int):
        with self.container.unit_of_work as uow:

            message = uow.Message.get_by_id(id)

            if not message:
                raise NotFoundError("message not found")

            media = None

            if message.media_id:
                media = uow.Media.get_by_id(message.media_id)

                if not media:
                    raise NotFoundError("media not found")

            return {
                "message": message,
                "media": media,
            }

    def get_media(self, id: int):
        with self.container.unit_of_work as uow:

            media = uow.Media.get_by_id(id)

            if not media:
                raise NotFoundError("media not found")

            media_file = self.container.storage_service.read_media(
                storage_name=media.stored_name,
                media_type=media.media_type,
            )

            mime_type, _ = mimetypes.guess_type(
                media.original_name
            )

            return Response(
                content=media_file,
                media_type=mime_type or "application/octet-stream",
            )

    def delete_message(self, id: int):
        with self.container.unit_of_work as uow:

            message = uow.Message.get_by_id(id)

            if not message:
                raise NotFoundError("message not found")

            if message.id:
                if uow.MessageTarget.exist_by_message_id(message.id):
                    return {
                        "success": False,
                        "message": "پیام زمانبندی شده است",
                    }

            uow.Message.delete(id)

        self._log("message deleted")

        return {
            "success": True,
            "message": "پیام با موفقیت حذف شد",
        }

    def update_message(
        self,
        id: int,
        text: str,
    ):
        with self.container.unit_of_work as uow:

            message = uow.Message.get_by_id(id)

            if not message:
                raise NotFoundError("message not found")

            message.update(text=text)

            uow.Message.update(message)

        self._log("message updated")

        return {
            "success": True,
            "message": "پیام با موفقیت ویرایش شد",
        }