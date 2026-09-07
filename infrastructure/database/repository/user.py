from domain.exeptions import ValidationError, NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from infrastructure.database.models import UserModel
from domain.entities import User
from infrastructure.database.mappers import UserMapper
from domain.repositories import IUserRepository


class UserRepository(SQLAlchemyRepository[UserModel], IUserRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = UserMapper()

    @property
    def model(self) -> type[UserModel]:
        return UserModel

    def create(self, entity: User):
        model = self.mapper.to_model(entity)
        model = super().create(model)

    def update(self, entity: User)->int :
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(f"User with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)
        return model.id

    def get_by_id(self, id: int) -> User | None:
        model = super().get_by_id(id)
        if model:
            entity = self.mapper.to_entity(model)
            return entity
        return None

    def get_all(self) -> list[User]:
        models = super().get_all()
        entities = []
        if models:

            for model in models:
                entities.append(self.mapper.to_entity(model))

        return entities

    def search_username(self, name: str) -> list[User]:
        query = select(UserModel).where(UserModel.user_name.ilike(f"%{name}%"))

        models = self.session.execute(query).scalars().all()

        return [self.mapper.to_entity(model) for model in models]
