from domain.entities.media import Media
from infrastructure.database.models.media import MediaModel


class MediaMapper:

    @staticmethod
    def to_model(entity: Media) -> MediaModel:
        return MediaModel(
            id=entity.id,
            message_id=entity.message_id,
            original_name=entity.original_name,
            stored_name=entity.stored_name,
            size=entity.size,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(model: MediaModel) -> Media:
        return Media(
            id=model.id,
            message_id=model.message_id,
            original_name=model.original_name,
            stored_name=model.stored_name,
            size=model.size,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def update_model(
        entity: Media,
        model: MediaModel,
    ) -> MediaModel:

        model.message_id = entity.message_id
        model.original_name = entity.original_name
        model.stored_name = entity.stored_name
        model.updated_at = entity.updated_at

        return model
