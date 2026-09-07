from dataclasses import dataclass


@dataclass(frozen=True)
class EntityActivatedEvent:
    entity_id: int
    entity_class_name: str
    source: str
