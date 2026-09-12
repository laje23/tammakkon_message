from typing import Any

from domain.interfaces import IEventBus


class EventBus(IEventBus):

    def __init__(self):
        self._listeners: dict[type, list[Any]] = {}

    def register(
        self,
        event_type: type,
        listener: Any,
    ) -> None:

        if event_type not in self._listeners:
            self._listeners[event_type] = []

        self._listeners[event_type].append(listener)

    def publish(
        self,
        event: Any,
    ) -> None:

        event_type = type(event)

        listeners = self._listeners.get(
            event_type,
            [],
        )

        for listener in listeners:
            listener.handle(event)