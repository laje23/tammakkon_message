from application.service import SendService
from infrastructure.dependency_Injection import container
from domain.exeptions import SendError
from domain.types import MessageTargetStatusType


async def send_message():
    sender = SendService()
    print("send message ")

    with container.unit_of_work as uow:
        print("send message : with ")
        messages = uow.MessageTarget.get_due()

    for message in messages:
        print("send message : for ")
        
        reasult = await sender.send_message(message)

        with container.unit_of_work as uow:
            if not reasult:
                print("send message : not result ")
                message.change_status(MessageTargetStatusType.FAILED)
                raise SendError("send message has an error and message not sent")
            else:
                print("send message : result ")
                message.change_status(MessageTargetStatusType.SENT)

            uow.MessageTarget.update(message)
