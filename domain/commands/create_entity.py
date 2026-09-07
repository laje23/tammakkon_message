from dataclasses import dataclass
from typing import Any
from domain.base import AppEntity


@dataclass
class CreateEntityCommand:
    def __init__(self, entity_class: type[AppEntity], **attributes: Any) -> None:
        self.attributes = attributes
        self.entity_class = entity_class
