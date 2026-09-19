from domain.interfaces import IUnitOfWork , IHashService , IAuthenticationService
from domain.types import PermissionType

class AuthenticationService(IAuthenticationService):
    
    def __init__(self , uow : IUnitOfWork , hash : IHashService) -> None:
        self.uow = uow
        self.hash = hash
    
    def add_role_to_user(self ,user_id : int , role_id:int):
        with self.uow as uow :
            self.uow.User.add_role(user_id , role_id)
    
    def remove_role_from_user(self ,user_id : int , role_id:int):
        with self.uow as uow :
            self.uow.User.remove_role(user_id , role_id)
    
    def get_role(self ,user_id : int):
        with self.uow as uow :
            return self.uow.User.get_roles(user_id)
    
    def check_permission(
        self,
        user_id: int,
        permission: PermissionType,
    ) -> bool:

        roles = self.get_role(user_id)
        if not roles:
            return False
        with self.uow as uow :
            for role in roles: 
                if role.id : 
                    permissions=uow.Role.get_permissions(role.id)
                    if permission in permissions :
                        return True
        return False
    
    def authenticate(self , username , password):
        with self.uow as uow :
            user =uow.User.get_by_username(username)
        if not user :
            return None
        
        if self.hash.verify(password , user.password) :
            return user 
        
    def get_user_permissions(self, user_id: int) -> list[PermissionType]:

        roles = self.get_role(user_id)

        if not roles:
            return []

        permissions = []

        with self.uow as uow:
            for role in roles:
                if role.id:
                    role_permissions = uow.Role.get_permissions(role.id)

                    for permission in role_permissions:
                        if permission not in permissions:
                            permissions.append(permission)

        return permissions