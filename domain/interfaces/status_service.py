from datetime import date
from domain.interfaces.unit_of_work import IUnitOfWork
from abc import ABC , abstractmethod



class IStatisticsService(ABC):
    @abstractmethod
    def __init__(self, unit_of_work: IUnitOfWork) -> None:
        ... 
        
    @abstractmethod
    def message_status(self) -> dict[date, dict[str, int]]:
        ...
        
    @abstractmethod
    def destination_status(self) -> dict[date, dict[str, int]]:
        ...