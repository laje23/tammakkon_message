from dataclasses import dataclass
from typing import Any
from domain.base import AppEntity


@dataclass
class ActivationEntityCommand:
    def __init__(self, entity_class: type[AppEntity], entity_id : int , activate: bool = False) -> None:
        self.entity_id = entity_id
        self.entity_class = entity_class
        self.activate = activate