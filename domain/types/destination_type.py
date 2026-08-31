from enum import Enum


class DestinationType(Enum):
    CHANNEL = "channel"
    GROUP = "group"
    SUPER_GROUP = "super_group"
    PRIVATE = "private"
