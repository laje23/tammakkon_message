from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from infrastructure.database.base import Base

ModelT = TypeVar("ModelT", bound=Base)


class SQLAlchemyRepository(Generic[ModelT]):

    def __init__(self, session: Session):
        self.session = session

    def create(self, model: ModelT) -> None:
        self.session.add(model)
        self.session.flush()
        self.session.refresh(model)

    def get_by_id(self, model_id: int) -> ModelT | None:
        return self.session.get(self.model, model_id)

    def get_all(self) -> list[ModelT]:
        statement = select(self.model)

        result = self.session.scalars(statement)

        return list(result)

    def delete(self, model: ModelT) -> None:
        self.session.delete(model)

    @property
    def model(self) -> type[ModelT]:
        raise NotImplementedError
