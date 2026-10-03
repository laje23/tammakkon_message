from application.service import SendService
from infrastructure.dependency_Injection import container
from domain.exeptions import SendError
from domain.types import MessageTargetStatusType


async def send_message():
    sender = SendService()

    with container.unit_of_work as uow:
        messages = uow.MessageTarget.get_due()

    for message in messages:
        reasult = await sender.send_message(message)

        with container.unit_of_work as uow:
            if not reasult:
                message.change_status(MessageTargetStatusType.FAILED)
                raise SendError("send message has an error and message not sent")
            else:
                message.change_status(MessageTargetStatusType.SENT)

            uow.MessageTarget.update(message)
