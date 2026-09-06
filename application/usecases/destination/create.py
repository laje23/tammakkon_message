from domain.entities import Destination
from domain.interfaces import IUnitOfWork, ILogger
from domain.types import DestinationType


class CreateDestinationUseCase:

    def __init__(
        self,
        uow: IUnitOfWork,
        logger: ILogger,
    ) -> None:
        self.logger = logger
        self.uow = uow

    def execute(
        self,
        external_id: str,
        name: str,
        bot_account_id: int | None,
        type: DestinationType,
    ):

        destination = Destination(None, external_id, name, bot_account_id, type)
        with self.uow as uow:
            uow.destination.create(destination)

        self.logger.log(
            f"destination {name} created",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__,
        )
