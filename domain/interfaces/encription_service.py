from abc import ABC , abstractmethod



class IEncription(ABC):
    
    @abstractmethod
    def encrip(self , text)->str :
        ...
    
    @abstractmethod
    def decrip(self , text)->str :
        ...