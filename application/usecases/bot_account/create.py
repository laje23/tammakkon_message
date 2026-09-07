from domain.entities import BotAccount
from domain.types import PlatformType
from domain.interfaces import IHashService, IUnitOfWork, IEventBus
from domain.events import EntityCreatedEvent

class CreateBotAccountUseCase:

    def __init__(
        self,
        hash_service: IHashService,
        uow: IUnitOfWork,
        event_bus:IEventBus
        
    ) ->None:
        self.hash_service = hash_service
        self.uow = uow
        self.event_bus = event_bus
        
    def execute(self, platform: PlatformType, name: str, token: str):
        token_hashed = self.hash_service.hash(token)
        bot_account = BotAccount(None, platform, name, token_hashed, True)

        with self.uow as uow:
            uow.bot_account.create(bot_account)

        self.event_bus.publish(
            EntityCreatedEvent(
                bot_account.__class__.__name__,
                bot_account.name,
                f"application/usecase : {self.__class__.__name__}"
            )
        )
