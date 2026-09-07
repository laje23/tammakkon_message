from domain.interfaces import IUnitOfWork, IEventBus
from domain.events import EntityDeletedEvent
from domain.exeptions import InvalidStateError
class DeleteDestinationUseCase:

    def __init__(
        self,
        uow: IUnitOfWork,
        event_bus : IEventBus,
    ) -> None:
        self.event_bus = event_bus
        self.uow = uow

    def execute(self, destination_id: int):

        with self.uow as uow:
            entity=uow.destination.get_by_id(destination_id)
            if not entity : 
                raise InvalidStateError("entity not in database")
            uow.destination.delete(destination_id)
            
        self.event_bus.publish(
            EntityDeletedEvent(
                entity.__class__.__name__,
                destination_id,
                f"application/uscase : {self.__class__.__name__}"
            )
        )