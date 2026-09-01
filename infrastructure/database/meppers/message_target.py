from domain.entities.message_target import MessageTarget
from infrastructure.database.models.message_target import MessageTargetModel


class MessageTargetMapper:

    @staticmethod
    def to_model(entity: MessageTarget) -> MessageTargetModel:
        return MessageTargetModel(
            id=entity.id,
            message_id=entity.message_id,
            destination_id=entity.destination_id,
            status=entity.status,
            retry_count=entity.retry_count,
            last_error=entity.last_error,
            send_at=entity.send_at,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(model: MessageTargetModel) -> MessageTarget:
        return MessageTarget(
            id=model.id,
            message_id=model.message_id,
            destination_id=model.destination_id,
            status=model.status,
            retry_count=model.retry_count,
            last_error=model.last_error,
            send_at=model.send_at,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def update_model(
        entity: MessageTarget,
        model: MessageTargetModel,
    ) -> MessageTargetModel:

        model.message_id = entity.message_id
        model.destination_id = entity.destination_id
        model.status = entity.status
        model.retry_count = entity.retry_count
        model.last_error = entity.last_error
        model.send_at = entity.send_at
        model.updated_at = entity.updated_at

        return model
