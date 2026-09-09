from domain.interfaces import IUnitOfWork, ICommandBus
from domain.commands import ProcessSendMessagesCommand , SendMessagesCommand
from domain.exeptions import OperationFailedError


class ProcessSendMessagesHandler:
    def __init__(self, unit_of_work: IUnitOfWork, command_bus: ICommandBus) -> None:
        self.unit_of_work = unit_of_work
        self.command_bus = command_bus



    def handle(self, command:ProcessSendMessagesCommand):
        message_torgets = command.message_targets
        for message_target in message_torgets:
            with self.unit_of_work as uow :
                message=uow.Message.get_by_id(message_target.message_id)
                
                destination=uow.Destination.get_by_id(message_target.destination_id)
                
                if message is None or destination is None :
                    raise OperationFailedError("message or destination is None")
                
                if destination.bot_account_id is None :
                    raise OperationFailedError("destination.bot_account_id is None")
                
                bot = uow.BotAccount.get_by_id(destination.bot_account_id)
                if bot is None:
                    raise OperationFailedError("bot is None")
                
                publish_command = SendMessagesCommand(
                    platform=bot.platform ,
                    chat_external_id=destination.external_id ,
                    message_type=message.type,
                    text= message.text,
                    medi_id=message.media_id
                    )
                
                
            self.command_bus.publish(
                publish_command
            )
            