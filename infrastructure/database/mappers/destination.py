from domain.entities.destination import Destination
from infrastructure.database.models.destination import DestinationModel


class DestinationMapper:

    @staticmethod
    def to_model(entity: Destination) -> DestinationModel:
        return DestinationModel(
            id=entity.id,
            external_id=entity.external_id,
            name=entity.name,
            bot_account_id=entity.bot_account_id,
            type=entity.type,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(model: DestinationModel) -> Destination:
        return Destination(
            id=model.id,
            external_id=model.external_id,
            name=model.name,
            bot_account_id=model.bot_account_id,
            type=model.type,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def update_model(
        entity: Destination,
        model: DestinationModel,
    ) -> DestinationModel:

        model.external_id = entity.external_id
        model.name = entity.name
        model.bot_account_id = entity.bot_account_id
        model.type = entity.type
        model.is_active = entity.is_active
        model.updated_at = entity.updated_at

        return model
