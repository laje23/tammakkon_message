from domain.events.update_entity import EntityUpdatedEvent
from domain.interfaces import ILogger


class CreateLogListener:
    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

    def handle(self, event: EntityUpdatedEvent) -> None:
        self.logger.log(
            f"entity {event.entity_class_name} with name :{event.entity_name} and id :{event.entity_id} updated",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            event.source,
        )
