from domain.events import EntityCreatedEvent
from domain.interfaces import ILogger


class CreateActivatedLogListener:
    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

    def handle(self, event: EntityCreatedEvent) -> None:
        self.logger.log(
            f"entity {event.entity_class_name} with id {event.entity_id} activated",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            event.source,
        )
