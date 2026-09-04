from domain.exeptions import ValidationError, NotFoundError
from domain.types.platform_type import PlatformType
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from infrastructure.database.models import UserAccountModel
from domain.entities import UserAccount
from infrastructure.database.mappers import UserAccountMapper
from domain.repositories import IUserAccountRepository


class UserAccountRepository(
    SQLAlchemyRepository[UserAccountModel], IUserAccountRepository
):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = UserAccountMapper()

    @property
    def model(self) -> type[UserAccountModel]:
        return UserAccountModel

    def create(self, entity: UserAccount):
        model = self.mapper.to_model(entity)
        model = super().create(model)

    def update(self, entity: UserAccount):
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(f"UserAccount with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)

    def get_by_id(self, id: int) -> UserAccount | None:
        model = super().get_by_id(id)
        if model:
            entity = self.mapper.to_entity(model)
            return entity
        return None

    def get_all(self) -> list[UserAccount]:
        models = super().get_all()
        entities = []
        if models:

            for model in models:
                entities.append(self.mapper.to_entity(model))

        return entities
