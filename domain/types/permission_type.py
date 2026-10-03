from enum import Enum


class PermissionType(Enum):

    MAIN = "main"
    STATUS = "status"
    MESSAGE = "message"
    USER = "user"
    SETTINGS = "settings"
    SCHEDULE = "schedule"
    DESTINATION = "destination"
    BOT = "bot"
