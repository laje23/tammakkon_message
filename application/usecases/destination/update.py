from domain.entities import Destination
from domain.interfaces import IUnitOfWork, ILogger
from domain.types import DestinationType


class UpdateDestinationUseCase:

    def __init__(
        self,
        uow: IUnitOfWork,
        logger: ILogger,
    ) -> None:
        self.logger = logger
        self.uow = uow

    def execute(
        self,
        entity: Destination,
        external_id: str,
        name: str,
        bot_account_id: int | None,
        type: DestinationType,
    ):

        entity.update(name, external_id, bot_account_id, type)
        with self.uow as uow:
            uow.destination.update(entity)

        self.logger.log(
            f"destination with id {entity.id} updated",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__,
        )
