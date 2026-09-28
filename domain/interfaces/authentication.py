from domain.types import PermissionType
from domain.entities import User
from abc import ABC, abstractmethod


class IAuthenticationService(ABC):

    @abstractmethod
    def add_role_to_user(self, user_id: int, role_id: int): ...
    @abstractmethod
    def remove_role_from_user(self, user_id: int, role_id: int): ...
    @abstractmethod
    def get_role(self, user_id: int): ...
    @abstractmethod
    def check_permission(
        self,
        user_id: int,
        permission: PermissionType,
    ) -> bool: ...

    @abstractmethod
    def authenticate(self, username, password) -> User | None: ...

    @abstractmethod
    def get_user_permissions(self, user_id: int) -> list[PermissionType]: ...
