from domain.entities import BotAccount
from domain.repositories import IBotAccountRepository
from domain.types import PlatformType
from domain.interfaces import IHashService, IUnitOfWork, ILogger


class CreateBotAccountUseCase:

    def __init__(
        self,
        repository: IBotAccountRepository,
        hash_service: IHashService,
        uow: IUnitOfWork,
        logger: ILogger,
    ) -> None:
        self.repo = repository
        self.hash_service = hash_service
        self.uow = uow
        self.logger = logger

    def execute(self, platform: PlatformType, name: str, token: str):
        token_hashed = self.hash_service.hash(token)
        bot_account = BotAccount(None, platform, name, token_hashed, True)

        with self.uow as uow:
            uow.bot_account.create(bot_account)

        self.logger.log(
            f"bout_account {name} created",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__,
        )
