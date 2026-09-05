from domain.entities import BotAccount
from domain.repositories import IBotAccountRepository
from domain.types import PlatformType
from domain.interfaces import IHashService , IUnitOfWork




class UpdateBotAccountUseCase():
    
    def __init__(self , repository: IBotAccountRepository, hash_service:IHashService , uow:IUnitOfWork) -> None:
        self.repo = repository
        self.hash_service = hash_service
        self.uow = uow 
        
    def execute(self ,bot_account:BotAccount , name:str|None = None , token : str|None = None , platform:PlatformType|None = None):

        token_hashed =self.hash_service.hash(token) if token else None
        
        bot_account.update(platform , name ,token_hashed)

        with self.uow as uow :
            uow.bot_account.update(bot_account)
            