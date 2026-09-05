from abc import ABC, abstractmethod

from domain.repositories import *


class IUnitOfWork(ABC):

    @property
    @abstractmethod
    def user(self) -> IUserRepository: ...

    @property
    @abstractmethod
    def role(self) -> IRoleRepository: ...

    @property
    @abstractmethod
    def bot_account(self) -> IBotAccountRepository: ...

    @property
    @abstractmethod
    def destination(self) -> IDestinationRepository: ...

    @property
    @abstractmethod
    def log(self) -> ILogRepository: ...

    @property
    @abstractmethod
    def message(self) -> IMessageRepository: ...

    @property
    @abstractmethod
    def media(self) -> IMediaRepository: ...

    @property
    @abstractmethod
    def user_account(self) -> IUserAccountRepository: ...

    @property
    @abstractmethod
    def message_target(self) -> IMessageTargetRepository: ...

    @abstractmethod
    def __enter__(self) -> "IUnitOfWork": ...

    @abstractmethod
    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None: ...
