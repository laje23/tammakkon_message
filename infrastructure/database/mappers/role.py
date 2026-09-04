from domain.entities.role import Role
from infrastructure.database.models.role import RoleModel


class RoleMapper:

    @staticmethod
    def to_model(entity: Role) -> RoleModel:
        return RoleModel(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(model: RoleModel) -> Role:
        return Role(
            id=model.id,
            name=model.name,
            description=model.description,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def update_model(
        entity: Role,
        model: RoleModel,
    ) -> RoleModel:
        model.name = entity.name
        model.description = entity.description
        model.updated_at = entity.updated_at

        return model
