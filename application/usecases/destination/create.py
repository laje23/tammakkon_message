from domain.entities import Destination
from domain.interfaces import IUnitOfWork , IEventBus
from domain.types import DestinationType
from domain.events import EntityCreatedEvent

class CreateDestinationUseCase:

    def __init__(
        self,
        uow: IUnitOfWork,
        event_bus : IEventBus
    ) -> None:
        self.uow = uow
        self.event_bus = event_bus

    def execute(
        self,
        external_id: str,
        name: str,
        bot_account_id: int | None,
        type: DestinationType,
    ):

        destination = Destination(None, external_id, name, bot_account_id, type)
        with self.uow as uow:
            uow.destination.create(destination)

        self.event_bus.publish(
            EntityCreatedEvent(
                destination.__class__.__name__,
                destination.name ,
                f"application/usecase : {self.__class__.__name__}"
            )
        )