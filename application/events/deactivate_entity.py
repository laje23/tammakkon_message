from dataclasses import dataclass


@dataclass(frozen=True)
class EntityDeactivatedEvent:
    entity_class_name: str
    entity_id: int
    source: str
