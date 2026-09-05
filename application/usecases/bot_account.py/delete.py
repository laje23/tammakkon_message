from domain.entities import BotAccount
from domain.repositories import IBotAccountRepository
from domain.interfaces import IUnitOfWork




class DeleteBotAccountUseCase():
    
    def __init__(self , repository: IBotAccountRepository, uow:IUnitOfWork) -> None:
        self.repo = repository
        self.uow = uow 
        
    def execute(self ,bot_account_id:int):

        with self.uow as uow :
            uow.bot_account.delete(bot_account_id)
            