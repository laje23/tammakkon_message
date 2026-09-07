from domain.entities import Destination
from domain.interfaces import IUnitOfWork, IEventBus
from domain.types import DestinationType
from domain.events import EntityUpdatedEvent

class UpdateDestinationUseCase:

    def __init__(
        self,
        uow: IUnitOfWork,
        event_bus: IEventBus,
    ) -> None:
        self.event_bus = event_bus
        self.uow = uow

    def execute(
        self,
        entity: Destination,
        external_id: str,
        name: str,
        bot_account_id: int | None,
        type: DestinationType,
    ):

        entity.update(name, external_id, bot_account_id, type)
        with self.uow as uow:
            uow.destination.update(entity)

        self.event_bus.publish(
            EntityUpdatedEvent(
                entity.__class__.__name__,
                name ,
                entity.id if entity.id else 0,
                f"application/usecase : {self.__class__.__name__}"
            )
        )