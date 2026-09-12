from domain.events import MessageSentEvent
from domain.interfaces import ILogger


class MessageSentHandler:
    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

    def handle(self, event: MessageSentEvent) -> None:
        self.logger.log(
            f"message with id {event.entity_id} sent in {event.sent_time}",
            self.logger.category.SYSTEM,
            self.logger.level.INFO,
            self.__class__.__name__,
        )
