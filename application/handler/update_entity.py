from domain.interfaces import IUnitOfWork, IEventBus
from application.commands import UpdateEntityCommand
from application.events import EntityUpdatedEvent
from domain.exeptions import OperationFailedError


class UpdateEntityHandler:
    def __init__(self, unit_of_work: IUnitOfWork, event_bus: IEventBus) -> None:
        self.unit_of_work = unit_of_work
        self.event_bus = event_bus

    def handle(self, command: UpdateEntityCommand):
        try:
            entity_class = command.entity_class
            entity = entity_class(**command.attributes)
        except Exception as e:
            raise OperationFailedError(str(e), details={"error": e})

        with self.unit_of_work as uow:
            repo = uow.get_repository(entity_class)
            entity_id = repo.update(entity)

        self.event_bus.publish(
            EntityUpdatedEvent(entity_id, entity_class.__name__, self.__class__.__name__)
        )
