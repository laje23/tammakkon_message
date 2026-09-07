from dataclasses import dataclass, field
from datetime import datetime
from domain.types import DestinationType
from domain.base import AppEntity


@dataclass
class Destination(AppEntity):
    id: int | None
    external_id: str
    name: str
    bot_account_id: int | None
    type: DestinationType
    is_active: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None

    def update(
        self,
        name: str | None = None,
        external_id: str | None = None,
        bot_account_id: int | None = None,
        type: DestinationType | None = None,
    ):
        if external_id is not None:
            self.external_id = external_id

        if bot_account_id is not None:
            self.bot_account_id = bot_account_id

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type

        self.updated_at = datetime.now()

    def activate(self):
        self.is_active = True
        self.updated_at = datetime.now()

    def deactivate(self):
        self.is_active = False
        self.updated_at = datetime.now()
