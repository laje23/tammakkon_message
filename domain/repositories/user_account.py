from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import UserAccount


class IUserAccountRepository(IBaseRepository[UserAccount]): ...
