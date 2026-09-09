from dataclasses import dataclass
from domain.types import PlatformType , MessageType


@dataclass
class SendMessagesCommand:
    platform:PlatformType 
    chat_external_id:str 
    message_type:MessageType 
    text:str 
    medi_id:int|None