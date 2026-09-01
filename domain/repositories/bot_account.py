from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import BotAccount


class IBotAccountRepository(IBaseRepository[BotAccount]): ...
