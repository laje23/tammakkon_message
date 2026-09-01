from dataclasses import dataclass, field
from datetime import datetime
from domain.types import LogCategory, LogLevel


@dataclass()
class Log:
    id: int | None
    category: LogCategory
    level: LogLevel
    message: str
    source: str
    created_at: datetime = field(default_factory=datetime.now)
