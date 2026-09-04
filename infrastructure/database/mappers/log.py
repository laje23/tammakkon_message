from domain.entities.log import Log
from infrastructure.database.models.log import LogModel


class LogMapper:

    @staticmethod
    def to_model(entity: Log) -> LogModel:
        return LogModel(
            id=entity.id,
            category=entity.category,
            level=entity.level,
            message=entity.message,
            source=entity.source,
            created_at=entity.created_at,
        )

    @staticmethod
    def to_entity(model: LogModel) -> Log:
        return Log(
            id=model.id,
            category=model.category,
            level=model.level,
            message=model.message,
            source=model.source,
            created_at=model.created_at,
        )
