from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Role:
    id: int | None
    name: str
    description: str | None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None

    def update(self, name: str | None = None, descrtiption: str | None = None):
        if name is not None:
            self.name = name

        if descrtiption is not None:
            self.descrtiption = descrtiption

        self.updated_at = datetime.now()
