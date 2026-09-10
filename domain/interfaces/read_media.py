from abc import ABC , abstractmethod



class IReadMedia(ABC):
    
    
    @abstractmethod
    def read(self , storge_name:str)-> bytes:
        ... 