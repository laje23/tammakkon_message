from domain.exeptions import ValidationError, NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session 
from sqlalchemy import select , delete 
from infrastructure.database.models import RoleModel
from domain.entities import Role
from infrastructure.database.mappers import RoleMapper
from domain.repositories import IRoleRepository
from domain.types import PermissionType
from infrastructure.database.relation_tables.role_permission import RolePermissionModel


class RoleRepository(SQLAlchemyRepository[RoleModel], IRoleRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = RoleMapper()

    @property
    def model(self) -> type[RoleModel]:
        return RoleModel

    def create(self, entity: Role):
        model = self.mapper.to_model(entity)
        model = super().create(model)
    
    def _get_role_or_raise(self, role_id: int) -> RoleModel:
        role = super().get_by_id(role_id)

        if role is None:
            raise NotFoundError(
                f"Role with id={role_id} not found"
            )

        return role

    def update(self, entity: Role):
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(f"Role with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)

    def get_by_id(self, id: int) -> Role | None:
        model = super().get_by_id(id)

        if model:
            return self.mapper.to_entity(model)

        return None

    def get_all(self) -> list[Role]:
        models = super().get_all()
        entities = []

        if models:
            for model in models:
                entities.append(self.mapper.to_entity(model))

        return entities

    def add_permission(
        self,
        role_id: int,
        permission: PermissionType,
    ) -> None:

        self._get_role_or_raise(role_id)

        query = select(RolePermissionModel).where(
            RolePermissionModel.role_id == role_id,
            RolePermissionModel.permission == permission.value,
        )

        existing = self.session.scalar(query)

        if existing is not None:
            return

        role_permission = RolePermissionModel(
            role_id=role_id,
            permission=permission.value,
        )

        self.session.add(role_permission)
        self.session.flush()

    def remove_permission(
        self,
        role_id: int,
        permission: PermissionType,
    ) -> None:

        self._get_role_or_raise(role_id)

        query = select(RolePermissionModel).where(
            RolePermissionModel.role_id == role_id,
            RolePermissionModel.permission == permission.value,
        )

        role_permission = self.session.scalar(query)

        if role_permission is None:
            raise NotFoundError(
                f"Permission '{permission.value}' "
                f"not found for role_id={role_id}"
            )

        self.session.delete(role_permission)
        self.session.flush()

        # حذف Permission
        delete_query = delete(RolePermissionModel).where(
            RolePermissionModel.role_id == role_id,
            RolePermissionModel.permission == permission.value,
        )

        self.session.execute(delete_query)
        self.session.flush()
        
    def has_permission(
        self,
        role_id: int,
        permission: PermissionType,
    ) -> bool:

        self._get_role_or_raise(role_id)

        query = select(RolePermissionModel).where(
            RolePermissionModel.role_id == role_id,
            RolePermissionModel.permission == permission.value,
        )

        return True if self.session.scalar(query) is not None else False
    
    
    def get_permissions(
        self,
        role_id: int,
    ) -> list[PermissionType]:

        self._get_role_or_raise(role_id)

        query = select(RolePermissionModel.permission).where(
            RolePermissionModel.role_id == role_id,
        )

        permissions = self.session.scalars(query).all()

        return [
            PermissionType(permission)
            for permission in permissions
        ]
        
    def clear_permissions(
        self,
        role_id: int,
    ) -> None:

        self._get_role_or_raise(role_id)

        query = delete(RolePermissionModel).where(
            RolePermissionModel.role_id == role_id,
        )

        self.session.execute(query)
        self.session.flush()

    def set_permissions(
        self,
        role_id: int,
        permissions: list[PermissionType],
    ) -> None:

        self._get_role_or_raise(role_id)

        # حذف Permissionهای قبلی
        delete_query = delete(RolePermissionModel).where(
            RolePermissionModel.role_id == role_id,
        )

        self.session.execute(delete_query)

        # حذف Permissionهای تکراری از لیست ورودی
        unique_permissions = set(permissions)

        # اضافه کردن Permissionهای جدید
        for permission in unique_permissions:
            role_permission = RolePermissionModel(
                role_id=role_id,
                permission=permission.value,
            )

            self.session.add(role_permission)

        self.session.flush()