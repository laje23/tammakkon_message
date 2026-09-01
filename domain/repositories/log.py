from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import Log
from domain.types import LogLevel, LogCategory


class ILogRepository(IBaseRepository[Log]):
    @abstractmethod
    def get_by_level(self, level: LogLevel) -> list[Log] | None: ...

    @abstractmethod
    def get_by_category(self, category: LogCategory) -> list[Log] | None: ...
