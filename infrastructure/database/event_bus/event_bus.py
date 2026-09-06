# infrastructure/event_bus/event_bus.py
from collections import defaultdict
from typing import Any


class EventBus:

    def __init__(self):
        self._listeners = defaultdict(list)

    def register(self, event_type: type, listener: Any) -> None:
        self._listeners[event_type].append(listener)

    def publish(self, event: Any) -> None:
        event_type = type(event)

        for listener in self._listeners[event_type]:
            listener.handle(event)
