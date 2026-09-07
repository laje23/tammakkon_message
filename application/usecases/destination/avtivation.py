from domain.entities import Destination
from domain.interfaces import IHashService, IUnitOfWork , IEventBus
from domain.events import EntityActivatedEvent , EntityDeactivatedEvent

class activationBotAccountUseCase:

    def __init__(
        self,
        hash_service: IHashService,
        uow: IUnitOfWork,
        event_bus : IEventBus
    ) -> None:
        self.hash_service = hash_service
        self.uow = uow
        self.event_bus = event_bus

    def activate(self, entity: Destination):
        entity.activate()

        with self.uow as uow:
            uow.destination.update(entity)
            
        self.event_bus.publish(
            EntityActivatedEvent(
                entity.__class__.__name__,
                entity.id if entity.id else 0,
                f"application/usecase : {self.__class__.__name__}"
            )
        )


    def deactivate(self, entity: Destination):
        entity.deactivate()

        with self.uow as uow:
            uow.destination.update(entity)


        self.event_bus.publish(
            EntityDeactivatedEvent(
                entity.__class__.__name__,
                entity.id if entity.id else 0,
                f"application/usecase : {self.__class__.__name__}"
            )
        )