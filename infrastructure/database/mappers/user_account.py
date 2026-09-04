from domain.entities.user_account import UserAccount
from infrastructure.database.models.user_account import UserAccountModel


class UserAccountMapper:

    @staticmethod
    def to_model(entity: UserAccount) -> UserAccountModel:
        return UserAccountModel(
            id=entity.id,
            user_id=entity.user_id,
            platform=entity.platform,
            account_id=entity.account_id,
            display_name=entity.display_name,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(model: UserAccountModel) -> UserAccount:
        return UserAccount(
            id=model.id,
            user_id=model.user_id,
            platform=model.platform,
            account_id=model.account_id,
            display_name=model.display_name,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def update_model(
        entity: UserAccount,
        model: UserAccountModel,
    ) -> UserAccountModel:
        model.display_name = entity.display_name
        model.updated_at = entity.updated_at

        return model
