from dataclasses import dataclass, field
from datetime import datetime
from domain.types import MessageType


@dataclass
class Message:
    id: int
    media_id: int | None
    type: MessageType
    text: str
    created_by: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None

    def update(self, media_id: int | None, type: MessageType | None, text: str | None):
        if media_id is not None:
            self.media_id = media_id
        if type is not None:
            self.type = type
        if text is not None:
            self.text = text

        self.updated_at = datetime.now()
