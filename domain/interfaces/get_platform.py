from domain.interfaces.send_app_service import ISender
from abc import ABC, abstractmethod
from domain.types import PlatformType


class IGetPlatform(ABC):

    @abstractmethod
    def get_platform(self, type: PlatformType) -> ISender: ...
