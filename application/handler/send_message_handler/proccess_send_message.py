from domain.interfaces import IUnitOfWork, IEventBus
from domain.commands import  SendMessagesCommand
from domain.exeptions import OperationFailedError


class ProcessSendMessagesHandler:
    def __init__(self, unit_of_work: IUnitOfWork, event_bus: IEventBus) -> None:
        self.unit_of_work = unit_of_work
        self.event_bus = event_bus



    def handle(self, command:SendMessagesCommand):
        