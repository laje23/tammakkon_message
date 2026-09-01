from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import User


class IUserRepository(IBaseRepository[User]):

    @abstractmethod
    def search_username(self, username: str) -> list[User] | None: ...
