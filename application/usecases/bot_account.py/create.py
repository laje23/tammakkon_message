from domain.entities import BotAccount
from domain.repositories import IBotAccountRepository
from domain.types import PlatformType
from domain.interfaces import IHashService

class CreateBotAccountUseCase():
    
    def __init__(self , repository: IBotAccountRepository, hash_service:IHashService) -> None:
        self.repo = repository
        self.hash_service = hash_service
        
    def execute(self ,platform: PlatformType ,  name :str , token : str):
        token_hashed =self.hash_service.hash(token)
        bot_account = BotAccount(None , platform , name , token_hashed , True)

