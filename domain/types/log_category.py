from enum import Enum


class LogCategory(str, Enum):
    SYSTEM = "system"
    AUTH = "auth"
    EXTERNAL = "external"
    DATABASE = "database"
    NETWORK = "network"