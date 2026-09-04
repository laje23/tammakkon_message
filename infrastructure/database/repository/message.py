from domain.exeptions import ValidationError, NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from infrastructure.database.models import MessageModel
from domain.entities import Message
from infrastructure.database.mappers import MessageMapper
from domain.repositories import IMessageRepository


class MessageRepository(SQLAlchemyRepository[MessageModel], IMessageRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = MessageMapper()

    @property
    def model(self) -> type[MessageModel]:
        return MessageModel

    def create(self, entity: Message):
        model = self.mapper.to_model(entity)
        model = super().create(model)

    def update(self, entity: Message):
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(f"Message with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)

    def get_by_id(self, id: int) -> Message | None:
        model = super().get_by_id(id)
        if model:
            entity = self.mapper.to_entity(model)
            return entity
        return None

    def get_all(self) -> list[Message]:
        models = super().get_all()
        entities = []
        if models:

            for model in models:
                entities.append(self.mapper.to_entity(model))

        return entities
