from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import BotAccount
from domain.types import PlatformType


class IBotAccountRepository(IBaseRepository[BotAccount]):

    @abstractmethod
    def get_by_platform(self, platform: PlatformType) -> list[BotAccount]: ...
