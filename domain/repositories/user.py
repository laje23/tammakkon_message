from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import User , Role

class IUserRepository(IBaseRepository[User]):

    @abstractmethod
    def search_username(self, username: str) -> list[User] | None: ...


    @abstractmethod
    def add_role(
        self,
        user_id: int,
        role_id: int,
    ) -> None:
        ...
    def remove_role(
        self,
        user_id: int,
        role_id: int,
    ) -> None:

        ...
    def get_roles(
        self,
        user_id: int,
    ) -> list[Role]:
        ...