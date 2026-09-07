from dataclasses import dataclass, field
from datetime import datetime
from domain.base import AppEntity


@dataclass
class User(AppEntity):
    id: int | None
    user_name: str
    password: str
    is_active: bool
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def update(self, user_name: str | None = None, password: str | None = None):
        if user_name is not None:
            self.user_name = user_name

        if password is not None:
            self.password = password

        self.updated_at = datetime.now()
