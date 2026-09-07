# domain/events/bot_account_created.py

from dataclasses import dataclass


@dataclass(frozen=True)
class EntityCreatedEvent:
    entity: object
    entity_class_name: str
    source: str
