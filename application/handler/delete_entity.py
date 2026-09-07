from domain.interfaces import IUnitOfWork, IEventBus
from application.commands import DeleteEntityCommand
from application.events import EntityDeletedEvent
from domain.exeptions import OperationFailedError


class DeleteEntityHandler:
    def __init__(self, unit_of_work: IUnitOfWork, event_bus: IEventBus) -> None:
        self.unit_of_work = unit_of_work
        self.event_bus = event_bus

    def handle(self, command: DeleteEntityCommand):
        
        with self.unit_of_work as uow:
            repo = uow.get_repository(command.entity_class)
            repo.delete(command.entity_id)

        self.event_bus.publish(
            EntityDeletedEvent(command.entity_id, command.entity_class.__name__, self.__class__.__name__)
        )
