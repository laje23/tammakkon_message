from domain.interfaces import IUnitOfWork, ILogger , IEventBus
from domain.events import  EntityDeletedEvent
from domain.exeptions import InvalidStateError

class DeleteBotAccountUseCase:

    def __init__(
        self, uow: IUnitOfWork, logger: ILogger , event_bus : IEventBus
    ) -> None:
        self.uow = uow
        self.logger = logger
        self.event_bus = event_bus

    def execute(self, bot_account_id: int):

        with self.uow as uow:
            entity=uow.bot_account.get_by_id(bot_account_id)
            if not entity : 
                raise InvalidStateError("entity not in database")
            uow.bot_account.delete(bot_account_id)

        self.event_bus.publish(
            EntityDeletedEvent(
                entity.__class__.__name__,
                bot_account_id,
                f"application/usecase : {self.__class__.__name__}"
            )
        )
