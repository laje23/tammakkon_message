from enum import Enum


class PermissionType(Enum):

    MAIN = "main"
    STATUS = "status"
    MESSAGE = "message"
    USER = "user"
    SETTINGS = "settings"
    LOG = "log"