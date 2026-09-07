from domain.interfaces import IUnitOfWork, IEventBus
from application.commands import ActivationEntityCommand 
from application.events import EntityActivatedEvent , EntityDeactivatedEvent
from domain.exeptions import OperationFailedError


class DeleteEntityHandler:
    def __init__(self, unit_of_work: IUnitOfWork, event_bus: IEventBus) -> None:
        self.unit_of_work = unit_of_work
        self.event_bus = event_bus

    def handle(self, command: ActivationEntityCommand):
        entity_id =command.entity_id
        entity_class = command.entity_class
        
        if command.activate :
            
            with self.unit_of_work as uow :
                repo=uow.get_repository(entity_class)
                entity=repo.get_by_id(entity_id)
                entity.activate()
                repo.update(entity)

            self.event_bus.publish(
                EntityActivatedEvent(command.entity_id, command.entity_class.__name__, self.__class__.__name__)
            )
        
        else:
        
            with self.unit_of_work as uow :
                repo=uow.get_repository(entity_class)
                entity=repo.get_by_id(entity_id)
                entity.deactivate()
                repo.update(entity)

        self.event_bus.publish(
            EntityDeactivatedEvent(command.entity_id, command.entity_class.__name__, self.__class__.__name__)
        )
