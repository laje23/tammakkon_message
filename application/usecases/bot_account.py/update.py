from domain.entities import BotAccount
from domain.repositories import IBotAccountRepository
from domain.types import PlatformType
from domain.interfaces import IHashService , IUnitOfWork , ILogger



class UpdateBotAccountUseCase():
    
    def __init__(self , repository: IBotAccountRepository, hash_service:IHashService , uow:IUnitOfWork , logger : ILogger) -> None:
        self.repo = repository
        self.hash_service = hash_service
        self.uow = uow 
        self.logger = logger 
        
    def execute(self ,bot_account:BotAccount , name:str|None = None , token : str|None = None , platform:PlatformType|None = None):

        token_hashed =self.hash_service.hash(token) if token else None
        
        bot_account.update(platform , name ,token_hashed)

        with self.uow as uow :
            uow.bot_account.update(bot_account)
        
        self.logger.log(
            f"bout_account with id {bot_account.id} updated",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__
        )