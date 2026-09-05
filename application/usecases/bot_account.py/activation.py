from domain.entities import BotAccount
from domain.repositories import IBotAccountRepository
from domain.types import PlatformType
from domain.interfaces import IHashService , IUnitOfWork , ILogger




class activationBotAccountUseCase():
    
    def __init__(self , repository: IBotAccountRepository, hash_service:IHashService , uow:IUnitOfWork , logger : ILogger) -> None:
        self.repo = repository
        self.hash_service = hash_service
        self.uow = uow 
        self.logger = logger
    
    def activate(self , entity: BotAccount):
        entity.activate()
        
        with self.uow as uow :
            uow.bot_account.update(entity)

    def deactivate(self , entity: BotAccount):
        entity.deactivate()
        
        with self.uow as uow :
            uow.bot_account.update(entity)
        
        self.logger.log(
            "bout_account created",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__
        )