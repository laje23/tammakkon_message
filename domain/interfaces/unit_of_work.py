from infrastructure.database.repository import *
from abc import ABC, abstractmethod
from typing import Self


class IUnitOfWork(ABC):

    def __init__(self): ...
    def __enter__(self) -> Self:
        return self

    @property
    @abstractmethod
    def User(self) -> UserRepository: ...
    @property
    @abstractmethod
    def Role(self) -> RoleRepository: ...
    @property
    @abstractmethod
    def BotAccount(self) -> BotAccountRepository: ...
    @property
    @abstractmethod
    def Destination(self) -> DestinationRepository: ...
    @property
    @abstractmethod
    def log(self) -> LogRepository: ...
    @property
    @abstractmethod
    def Message(self) -> MessageRepository: ...
    @property
    @abstractmethod
    def Media(self) -> MediaRepository: ...
    @property
    @abstractmethod
    def UserAccount(self) -> UserAccountRepository: ...
    @property
    @abstractmethod
    def MessageTarget(self) -> MessageTargetRepository: ...

    def get_repository(self, entity_type: type):
        return getattr(self, entity_type.__name__)

    def __exit__(self, exc_type, exc_value, traceback): ...
