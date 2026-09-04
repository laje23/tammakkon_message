from domain.exeptions import ValidationError, NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from infrastructure.database.models import DestinationModel
from domain.entities import Destination
from infrastructure.database.mappers import DestinationMapper
from domain.repositories import IDestinationRepository
from domain.types import DestinationType


class BotAccountRepository(
    SQLAlchemyRepository[DestinationModel], IDestinationRepository
):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = DestinationMapper()

    @property
    def model(self) -> type[DestinationModel]:
        return DestinationModel

    def create(self, entity: Destination):
        model = self.mapper.to_model(entity)
        model = super().create(model)

    def update(self, entity: Destination):
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(f"Destination with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)

    def delete(self, entity: Destination) -> None:
        model = self.mapper.to_model(entity)
        super().delete(model)

    def get_by_id(self, id: int) -> Destination | None:
        model = super().get_by_id(id)
        if model:
            entity = self.mapper.to_entity(model)
            return entity
        return None

    def get_all(self) -> list[Destination]:
        models = super().get_all()
        entities = []
        if models:

            for model in models:
                entities.append(self.mapper.to_entity(model))

        return entities

    def get_by_type(self, destination_type: DestinationType) -> list[Destination]:

        query = select(DestinationModel).where(
            DestinationModel.type == destination_type
        )
        entities = []
        models = self.session.execute(query).scalars().all()

        for model in models:
            entities.append(self.mapper.to_entity(model))

        return entities

    def get_by_bot_account(self, bot_account_id: int) -> list[Destination]:

        query = select(DestinationModel).where(
            DestinationModel.bot_account_id == bot_account_id
        )

        entities = []
        models = self.session.execute(query).scalars().all()

        for model in models:
            entities.append(self.mapper.to_entity(model))

        return entities
