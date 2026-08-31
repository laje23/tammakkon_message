from dataclasses import dataclass , field
from datetime import datetime
from domain.types.platform_type import PlatformType 

@dataclass
class BotAccount():
    id : int 
    platform : PlatformType
    name : str 
    token : str 
    is_active: bool
    created_at : datetime = field(default_factory=datetime.now)
    updated_at : datetime|None = None

    def update(self , platform:PlatformType |None , name: str|None, token:str|None):
        if token is not None :
            self.token = token
        if platform is not None :
            self.platform = platform
        if name is not None :
            self.name = name
        self.updated_at = datetime.now()
    
    
    def activate(self):
        self.is_active = True
        self.updated_at = datetime.now()
        
    
    
    def deactivate(self):
        self.is_active = False
        self.updated_at = datetime.now()