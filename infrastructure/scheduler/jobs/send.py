from application.service import SendService
from infrastructure.dependency_Injection import container

async def send_message():
    sender =SendService()
    with container.unit_of_work as uow :
        messages=uow.MessageTarget.get_due()
    for message in messages :
        await sender.send_message(message)