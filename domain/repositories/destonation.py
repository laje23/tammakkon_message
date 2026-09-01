from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import Destination


class IDestinationRepository(IBaseRepository[Destination]): ...
