# domain/events/bot_account_created.py

from dataclasses import dataclass


@dataclass(frozen=True)
class EntityUpdatedEvent:
    entity_id: int
    entity_class_name: str
    source: str
