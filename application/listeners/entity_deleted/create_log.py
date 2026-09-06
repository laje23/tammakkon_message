from domain.events import EntityDeletedEvent
from domain.interfaces import ILogger


class CreateLogListener:
    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

    def handle(self, event: EntityDeletedEvent) -> None:
        self.logger.log(
            f"entity {event.entity_class_name} with id:{event.entity_id} deleted",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            event.source,
        )
