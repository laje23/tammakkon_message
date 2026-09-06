# domain/events/bot_account_created.py

from dataclasses import dataclass


@dataclass(frozen=True)
class EntityCreatedEvent:
    entity_class_name: str
    entity_name: str
    source: str
