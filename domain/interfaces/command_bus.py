from typing import Any
from abc import ABC, abstractmethod


class ICommandBus(ABC):

    @abstractmethod
    def register(self, command_type: type, handler: Any) -> None: ...

    @abstractmethod
    def publish(self, command: Any) -> None: ...
