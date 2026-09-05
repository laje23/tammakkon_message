from domain.entities import BotAccount
from domain.repositories import IBotAccountRepository
from domain.types import PlatformType
from domain.interfaces import IHashService , IUnitOfWork




class activationBotAccountUseCase():
    
    def __init__(self , repository: IBotAccountRepository, hash_service:IHashService , uow:IUnitOfWork) -> None:
        self.repo = repository
        self.hash_service = hash_service
        self.uow = uow 
    
    def activate(self , entity: BotAccount):
        entity.activate()
        
        with self.uow as uow :
            uow.bot_account.update(entity)

    def deactivate(self , entity: BotAccount):
        entity.deactivate()
        
        with self.uow as uow :
            uow.bot_account.update(entity)
