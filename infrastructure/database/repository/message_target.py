from domain.exeptions import ValidationError, NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from infrastructure.database.models import MessageTargetModel
from domain.entities import MessageTarget
from infrastructure.database.mappers import MessageTargetMapper
from domain.repositories import IMessageTargetRepository


class MessageTargetRepository(
    SQLAlchemyRepository[MessageTargetModel], IMessageTargetRepository
):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = MessageTargetMapper()

    @property
    def model(self) -> type[MessageTargetModel]:
        return MessageTargetModel

    def create(self, entity: MessageTarget):
        model = self.mapper.to_model(entity)
        model = super().create(model)

    def update(self, entity: MessageTarget):
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(f"MessageTarget with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)

    def get_by_id(self, id: int) -> MessageTarget | None:
        model = super().get_by_id(id)
        if model:
            entity = self.mapper.to_entity(model)
            return entity
        return None

    def get_all(self) -> list[MessageTarget]:
        models = super().get_all()
        entities = []
        if models:

            for model in models:
                entities.append(self.mapper.to_entity(model))

        return entities
