from domain.exeptions import ValidationError, NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from infrastructure.database.models import MessageTargetModel
from domain.entities import MessageTarget
from infrastructure.database.mappers import MessageTargetMapper
from domain.repositories import IMessageTargetRepository
from datetime import datetime, timedelta
from domain.types import MessageTargetStatusType


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

    def update(self, entity: MessageTarget) -> int:
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(f"MessageTarget with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)
        return model.id

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

    def get_due(self) -> list[MessageTarget]:
        query = select(self.model).where(
            and_(
                self.model.send_at <= datetime.now(),
                self.model.status == MessageTargetStatusType.PENDING,
            )
        )
        models = self.session.execute(query).scalars().all()

        entities = []
        if models:

            for model in models:
                entities.append(self.mapper.to_entity(model))
        return entities

    def get_today_messages(self) -> list[MessageTarget]:
        today = datetime.today().date()

        start_of_day = datetime.combine(today, datetime.min.time())
        start_of_tomorrow = start_of_day + timedelta(days=1)

        query = select(self.model).where(
            and_(
                self.model.created_at >= start_of_day,
                self.model.created_at < start_of_tomorrow,
            )
        )

        models = self.session.execute(query).scalars().all()

        entities = []

        for model in models:
            entities.append(self.mapper.to_entity(model))

        return entities

    def exist_by_message_id(self, message_id: int):
        query = select(self.model).where(self.model.message_id == message_id)

        return self.session.execute(query).first() is not None
