from domain.entities import BotAccount
from domain.repositories import IBotAccountRepository
from domain.interfaces import IUnitOfWork , ILogger




class DeleteBotAccountUseCase():
    
    def __init__(self , repository: IBotAccountRepository, uow:IUnitOfWork , logger :ILogger) -> None:
        self.repo = repository
        self.uow = uow 
        self.logger = logger 
        
    def execute(self ,bot_account_id:int):

        with self.uow as uow :
            uow.bot_account.delete(bot_account_id)
        
        self.logger.log(
            f"bout_account with id {bot_account_id} deleted",
            self.logger.category.AUTH,
            self.logger.level.INFO,
            self.__class__.__name__
        )