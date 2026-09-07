from collections import defaultdict
from typing import Any


class EventBus:

    def __init__(self):
        self._listeners = defaultdict(list)

    def register(self, command_tpye: type, hendler: Any) -> None:
        self._listeners[command_tpye].append(hendler)

    def publish(self, event: Any) -> None:
        command_tpye = type(event)

        for hendler in self._listeners[command_tpye]:
            hendler.handle(event)
