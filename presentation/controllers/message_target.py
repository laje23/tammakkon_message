from infrastructure.dependency_Injection import container
from presentation.controllers.decorators import safe_class

from domain.entities import MessageTarget
from domain.types import MessageTargetStatusType
from domain.exeptions import NotFoundError


@safe_class
class MessageTargetController:

    def get_all_message_target(self):
        with container.unit_of_work as uow:
            return uow.MessageTarget.get_all()

    def get_all_message_target_with_details(self):
        with container.unit_of_work as uow:
            return uow.MessageTarget.get_all_with_details()

    def get_message_target_by_id(self, id):
        with container.unit_of_work as uow:
            target = uow.MessageTarget.get_by_id(id)

            if not target:
                raise NotFoundError("message target not found")

            return target

    def create_message_target(self, data):
        target = MessageTarget(
            None,
            data.message_id,
            data.destination_id,
            MessageTargetStatusType.PENDING,
            0,
            None,
            data.send_at,
        )

        with container.unit_of_work as uow:
            uow.MessageTarget.create(target)

        return {
            "success": True,
            "message": "زمانبندی پیام ثبت شد",
        }

    def delete_message_target(self, id):
        with container.unit_of_work as uow:
            target = uow.MessageTarget.get_by_id(id)

            if not target:
                raise NotFoundError("message target not found")

            uow.MessageTarget.delete(id)

        return {
            "success": True,
            "message": "زمانبندی پیام حذف شد",
        }

    def cancel_message_target(self, id):
        with container.unit_of_work as uow:
            target = uow.MessageTarget.get_by_id(id)

            if not target:
                raise NotFoundError("message target not found")

            target.cancel()
            uow.MessageTarget.update(target)

        return {
            "success": True,
            "message": "زمانبندی پیام لغو شد",
        }

    def resume_message_target(self, id):
        with container.unit_of_work as uow:
            target = uow.MessageTarget.get_by_id(id)

            if not target:
                raise NotFoundError("message target not found")

            target.resume()
            uow.MessageTarget.update(target)

        return {
            "success": True,
            "message": "زمانبندی پیام از سرگیری شد",
        }
