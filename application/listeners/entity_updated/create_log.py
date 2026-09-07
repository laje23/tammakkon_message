from application.events import EntityUpdatedEvent
from domain.interfaces import ILogger


class CreateUpdatedLogListener:
    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

    def handle(self, event: EntityUpdatedEvent) -> None:
        self.logger.log(
            f"entity {event.entity_class_name} with id :{event.entity_id} updated",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            event.source,
        )
