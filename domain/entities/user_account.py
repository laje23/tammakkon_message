from dataclasses import dataclass , field 
from datetime import datetime 
from domain.types import PlatformType


@dataclass
class UserAccount:
    id :int|None
    user_id : int
    platform : PlatformType
    account_id : str
    display_name : str | None
    created_at : datetime = field(default_factory=datetime.now)
    updated_at : datetime|None = None
    
    
    def update(self , display_name:str):
        self.display_name = display_name
        self.updated_at = datetime.now()