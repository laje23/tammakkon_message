from dataclasses import dataclass, field
from datetime import datetime

from domain.types.message_target_status import MessageTargetStatusType
from domain.base import AppEntity
from domain.exeptions import InvalidStateError

@dataclass
class MessageTarget(AppEntity):
    id: int | None
    message_id: int
    destination_id: int
    status: MessageTargetStatusType
    retry_count: int = 0
    last_error: str | None = None
    send_at: datetime | None = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None

    def change_status(self, status: MessageTargetStatusType):
        self.status = status
        self.updated_at = datetime.now()

    def increase_retry_count(self):
        self.retry_count += 1
        self.updated_at = datetime.now()

    def save_last_error(self, error: str):
        self.last_error = error
        self.updated_at = datetime.now()

    def cancel(self):
        if self.status != MessageTargetStatusType.PENDING:
            raise InvalidStateError(
                "only pending message targets can be canceled"
            )
        self.status = MessageTargetStatusType.CANCELED
        self.updated_at = datetime.now()

    def resume(self):
        if self.status != MessageTargetStatusType.CANCELED:
            raise InvalidStateError(
                "only canceled message targets can be resume"
            )
        self.status = MessageTargetStatusType.PENDING
        self.updated_at = datetime.now()
