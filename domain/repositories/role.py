from abc import abstractmethod
from domain.repositories import IBaseRepository
from domain.entities import Role


class IRoleRepository(IBaseRepository[Role]): ...
