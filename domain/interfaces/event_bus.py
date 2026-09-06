from typing import Any
from abc import ABC, abstractmethod


class IEventBus(ABC):

    @abstractmethod
    def register(self, event_type: type, listener: Any) -> None: ...

    @abstractmethod
    def publish(self, event: Any) -> None: ...
