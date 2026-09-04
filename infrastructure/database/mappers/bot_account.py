from domain.entities.bot_account import BotAccount
from infrastructure.database.models.bot_account import BotAccountModel


class BotAccountMapper:

    @staticmethod
    def to_model(entity: BotAccount) -> BotAccountModel:
        return BotAccountModel(
            id=entity.id,
            platform=entity.platform,
            name=entity.name,
            token=entity.token,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(model: BotAccountModel) -> BotAccount:
        return BotAccount(
            id=model.id,
            platform=model.platform,
            name=model.name,
            token=model.token,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def update_model(
        entity: BotAccount,
        model: BotAccountModel,
    ) -> BotAccountModel:

        model.platform = entity.platform
        model.name = entity.name
        model.token = entity.token
        model.is_active = entity.is_active
        model.updated_at = entity.updated_at

        return model
