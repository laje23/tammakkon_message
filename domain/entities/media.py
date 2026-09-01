from dataclasses import dataclass , field 
from datetime import datetime


@dataclass
class Media :
    id : int 
    message_id : int
    original_name : str 
    stored_name : str 
    size : int 
    created_at : datetime = field(default_factory=datetime.now)
    updated_at : datetime | None = None
    
    
    def update(self , message_id:int|None=None,original_name:str|None=None , stored_name : str|None=None):
        if message_id is not None:
            self.message_id = message_id
            
        if stored_name is not None:
            self.stored_name = stored_name
            
        if original_name is not None:
            self.original_name = original_name
        
        self.updated_at = datetime.now()