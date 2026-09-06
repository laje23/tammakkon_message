from domain.entities import Destination
from domain.interfaces import IUnitOfWork, ILogger


class activationDestinationUseCase:

    def __init__(
        self,
        uow: IUnitOfWork,
        logger: ILogger,
    ) -> None:
        self.uow = uow
        self.logger = logger

    def activate(self, entity: Destination):
        entity.activate()

        with self.uow as uow:
            uow.destination.update(entity)

        self.logger.log(
            "destination activated",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__,
        )
    def deactivate(self, entity: Destination):
        entity.deactivate()

        with self.uow as uow:
            uow.destination.update(entity)

        self.logger.log(
            "destination deactivated",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__,
        )
