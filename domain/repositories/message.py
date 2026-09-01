from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import Message


class IMessageRepository(IBaseRepository[Message]): ...
