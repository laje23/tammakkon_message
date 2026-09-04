from domain.exeptions import ValidationError, NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from infrastructure.database.models import MediaModel
from domain.entities import Media
from infrastructure.database.mappers import MediaMapper
from domain.repositories import IMediaRepository


class MediaRepository(SQLAlchemyRepository[MediaModel], IMediaRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = MediaMapper()

    @property
    def model(self) -> type[MediaModel]:
        return MediaModel

    def create(self, entity: Media):
        model = self.mapper.to_model(entity)
        model = super().create(model)

    def update(self, entity: Media):
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(f"Media with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)

    def get_by_id(self, id: int) -> Media | None:
        model = super().get_by_id(id)
        if model:
            entity = self.mapper.to_entity(model)
            return entity
        return None

    def get_all(self) -> list[Media]:
        models = super().get_all()
        entities = []
        if models:

            for model in models:
                entities.append(self.mapper.to_entity(model))

        return entities
