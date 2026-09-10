from abc import ABC , abstractmethod



class ISender(ABC):
    
    @abstractmethod
    def send_text(self ,chat_id : str , token:str ,text: str, file : bytes | None = None)-> bool:
        ...
    
    @abstractmethod
    def send_photo(self , chat_id : str , token: str , text:str , file: bytes)-> bool:
        ...
        
    @abstractmethod
    def send_audio(self , chat_id : str , token: str , text:str , file: bytes)-> bool:
        ...
        
    @abstractmethod
    def send_video(self , chat_id : str , token: str , text:str , file: bytes)-> bool:
        ...
        
    @abstractmethod
    def send_document(self , chat_id : str , token: str , text:str , file: bytes)-> bool:
        ...