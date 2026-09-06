from domain.events import EntityCreatedEvent
from domain.interfaces import ILogger


class CreateLogListener:
    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

    def handle(self, event: EntityCreatedEvent) -> None:
        self.logger.log(
            f"entity {event.entity_class_name} with name {event.entity_name} created",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            event.source,
        )
