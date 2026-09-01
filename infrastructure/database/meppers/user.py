from domain.entities.user import User
from infrastructure.database.models.user import UserModel


class UserMapper:

    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            user_name=entity.user_name,
            password=entity.password,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(model: UserModel) -> User:
        return User(
            id=model.id,
            user_name=model.user_name,
            password=model.password,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def update_model(
        entity: User,
        model: UserModel,
    ) -> UserModel:
        model.user_name = entity.user_name
        model.password = entity.password
        model.is_active = entity.is_active
        model.updated_at = entity.updated_at

        return model
