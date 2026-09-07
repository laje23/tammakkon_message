from dataclasses import dataclass, field
from datetime import datetime
from domain.types import LogCategory, LogLevel
from domain.base import AppEntity


@dataclass()
class Log(AppEntity):
    id: int | None
    category: LogCategory
    level: LogLevel
    message: str
    source: str
    created_at: datetime = field(default_factory=datetime.now)
