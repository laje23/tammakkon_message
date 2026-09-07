from dataclasses import dataclass
from typing import Any
from domain.base import AppEntity
from domain.entities import MessageTarget

@dataclass
class SendMessagesCommand:
    def __init__(self, message_targets:list[MessageTarget]) -> None:
        self.message_targets =message_targets
