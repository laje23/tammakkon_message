from domain.interfaces import (
    IUnitOfWork,
    IHashService,
    IAuthenticationService,
)
from domain.types import PermissionType


class AuthenticationService(IAuthenticationService):

    def __init__(
        self,
        uow: IUnitOfWork,
        hash: IHashService,
    ) -> None:
        self.uow = uow
        self.hash = hash

    def authenticate(
        self,
        username: str,
        password: str,
    ):
        with self.uow as uow:

            user = uow.User.get_by_username(username)

            if user is None:
                return None

            if not self.hash.verify(
                password,
                user.password,
            ):
                return None

            return user

    def add_role_to_user(
        self,
        user_id: int,
        role_id: int,
    ):
        with self.uow as uow:
            uow.User.add_role(
                user_id,
                role_id,
            )

    def remove_role_from_user(
        self,
        user_id: int,
        role_id: int,
    ):
        with self.uow as uow:
            uow.User.remove_role(
                user_id,
                role_id,
            )

    def get_role(
        self,
        user_id: int,
    ):
        with self.uow as uow:
            return uow.User.get_roles(user_id)

    def check_permission(
        self,
        user_id: int,
        permission: PermissionType,
    ) -> bool:

        roles = self.get_role(user_id)

        if not roles:
            return False

        with self.uow as uow:

            for role in roles:

                if not role.id:
                    continue

                permissions = uow.Role.get_permissions(role.id)

                if permission in permissions:
                    return True

        return False

    def get_user_permissions(
        self,
        user_id: int,
    ) -> list[PermissionType]:

        roles = self.get_role(user_id)

        if not roles:
            return []

        permissions = []

        with self.uow as uow:

            for role in roles:

                if not role.id:
                    continue

                role_permissions = uow.Role.get_permissions(role.id)

                for permission in role_permissions:

                    if permission not in permissions:
                        permissions.append(permission)

        return permissions
