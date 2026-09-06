from domain.entities import Destination
from domain.interfaces import IUnitOfWork, ILogger
from domain.types import DestinationType

class CreateBotAccountUseCase:

    def __init__(
        self,
        uow:IUnitOfWork,
        logger: ILogger,
    ) -> None:
        self.logger = logger
        self.uow = uow 
    def execute(self,destination_id : int ):
        

        with self.uow as uow:
            uow.destination.delete(destination_id)

        self.logger.log(
            f"destination with id {destination_id} created",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__,
        )
