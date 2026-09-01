from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import MessageTarget


class IMessageTargetRepository(IBaseRepository[MessageTarget]): ...
