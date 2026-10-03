from dataclasses import dataclass, field
from datetime import datetime

from domain.base import AppEntity
from domain.types import MediaType


@dataclass
class Media(AppEntity):
    id: int | None
    original_name: str
    stored_name: str
    media_type: MediaType
    size: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None

    def update(
        self,
        original_name: str | None = None,
        stored_name: str | None = None,
        media_type: MediaType | None = None,
    ):
        if original_name is not None:
            self.original_name = original_name

        if stored_name is not None:
            self.stored_name = stored_name

        if media_type is not None:
            self.media_type = media_type

        self.updated_at = datetime.now()
