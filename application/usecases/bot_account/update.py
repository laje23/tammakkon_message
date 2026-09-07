from domain.entities import BotAccount
from domain.types import PlatformType
from domain.interfaces import IHashService, IUnitOfWork,IEventBus
from domain.events import EntityUpdatedEvent

class UpdateBotAccountUseCase:

    def __init__(
        self,
        hash_service: IHashService,
        uow: IUnitOfWork,
        event_bus : IEventBus
    ) -> None:
        self.hash_service = hash_service
        self.uow = uow  
        self.event_bus =event_bus

    def execute(
        self,
        bot_account: BotAccount,
        name: str | None = None,
        token: str | None = None,
        platform: PlatformType | None = None,
    ):

        token_hashed = self.hash_service.hash(token) if token else None

        bot_account.update(platform, name, token_hashed)

        with self.uow as uow:
            uow.bot_account.update(bot_account)

        self.event_bus.publish(
            EntityUpdatedEvent(
                bot_account.__class__.__name__,
                None,
                bot_account.id if bot_account.id is not None else 0,
                f"application/usecase : {self.__class__.__name__}"
            )
        )