from domain.interfaces import IUnitOfWork , ICommandBus
from domain.commands import SendMessagesCommand

class ProccessCron:
    def __init__(self , unit_of_work : IUnitOfWork , command_bus : ICommandBus) -> None:
        self.unit_of_work = unit_of_work
        self.command_bus =command_bus
    
    
    def send_command(self, entities)->None:
        self.command_bus.publish(
            SendMessagesCommand(
                message_targets=entities
            )
        )
    
    def proccess(self):
        with self.unit_of_work as uow :
            entities=uow.MessageTarget.get_due()
        
        if entities :
            self.send_command(entities)
