from domain.entities.message import Message
from infrastructure.database.models.message import MessageModel


class MessageMapper:

    @staticmethod
    def to_model(entity: Message) -> MessageModel:
        return MessageModel(
            id=entity.id,
            media_id=entity.media_id,
            type=entity.type,
            text=entity.text,
            created_by=entity.created_by,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(model: MessageModel) -> Message:
        return Message(
            id=model.id,
            media_id=model.media_id,
            type=model.type,
            text=model.text,
            created_by=model.created_by,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def update_model(
        entity: Message,
        model: MessageModel,
    ) -> MessageModel:

        model.media_id = entity.media_id
        model.type = entity.type
        model.text = entity.text
        model.updated_at = entity.updated_at

        return model
