from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from infrastructure.database.models import LogModel
from domain.entities import Log
from infrastructure.database.mappers import LogMapper
from domain.repositories import ILogRepository
from domain.types import LogLevel, LogCategory


class LogRepository(SQLAlchemyRepository[LogModel], ILogRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = LogMapper()

    @property
    def model(self) -> type[LogModel]:
        return LogModel

    def create(self, entity: Log):
        model = self.mapper.to_model(entity)
        model = super().create(model)

    def get_by_id(self, id: int) -> Log | None:
        model = super().get_by_id(id)
        if model:
            entity = self.mapper.to_entity(model)
            return entity
        return None

    def get_all(self) -> list[Log]:
        models = super().get_all()
        entities = []
        if models:

            for model in models:
                entities.append(self.mapper.to_entity(model))

        return entities

    def get_by_category(self, category: LogCategory) -> list[Log]:

        query = select(LogModel).where(LogModel.category == category)
        entities = []
        models = self.session.execute(query).scalars().all()

        for model in models:
            entities.append(self.mapper.to_entity(model))

        return entities

    def get_by_level(self, level: LogLevel) -> list[Log]:

        query = select(LogModel).where(LogModel.level == LogCategory)

        entities = []
        models = self.session.execute(query).scalars().all()

        for model in models:
            entities.append(self.mapper.to_entity(model))

        return entities

    def update(self) -> None:
        return None