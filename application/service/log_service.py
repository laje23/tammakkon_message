from domain.entities import Log
from domain.types import LogCategory, LogLevel
from domain.interfaces import IUnitOfWork


class LogService:
    category = LogCategory
    level = LogLevel

    def __init__(self, uow: IUnitOfWork) -> None:
        self.uow = uow

    def log(
        self,
        message: str,
        category: LogCategory,
        level: LogLevel,
        source: str,
    ) -> None:

        log = Log(
            id=None,
            category=category,
            level=level,
            message=message,
            source=source,
        )

        self.uow.log.create(log)