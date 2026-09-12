from typing import Any

from domain.interfaces import ICommandBus


class CommandBus(ICommandBus):

    def __init__(self):
        self._handlers: dict[type, Any] = {}

    def register(
        self,
        command_type: type,
        handler: Any,
    ) -> None:

        self._handlers[command_type] = handler

    def publish(
        self,
        command: Any,
    ) -> None:

        command_type = type(command)

        handler = self._handlers.get(command_type)

        if handler is None:
            raise ValueError(
                f"No handler registered for "
                f"{command_type.__name__}"
            )

        handler.handle(command)