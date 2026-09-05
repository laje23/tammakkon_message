from abc import ABC, abstractmethod

from domain.types import LogCategory, LogLevel


class ILogger(ABC):
    category = LogCategory
    level = LogLevel

    @abstractmethod
    def log(
        self,
        message: str,
        category: LogCategory,
        level: LogLevel,
        source: str,
    ) -> None: ...
