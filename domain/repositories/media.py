from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import Media


class IMediaRepository(IBaseRepository[Media]): ...
