# domain/events/bot_account_created.py

from dataclasses import dataclass


@dataclass(frozen=True)
class EntityUpdatedEvent:
    entity_class_name: str
    entity_name: str
    entity_id: int
    source: str
