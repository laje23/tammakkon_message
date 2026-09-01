from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import UserAccount
from domain.types import PlatformType


class IUserAccountRepository(IBaseRepository[UserAccount]):

    @abstractmethod
    def get_by_platform(self, platform: PlatformType) -> list[UserAccount] | None: ...
