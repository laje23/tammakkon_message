from dataclasses import dataclass


@dataclass(frozen=True)
class EntityActivatedEvent:
    entity_class_name: str
    entity_id: int
    source: str
