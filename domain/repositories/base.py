from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class IBaseRepository(ABC, Generic[T]):

    @abstractmethod
    def create(self, entity: T) -> int:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> T | None:
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> None:
        pass
