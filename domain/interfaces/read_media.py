from abc import ABC, abstractmethod
from domain.types import MediaType

class IStorageService(ABC):

    @abstractmethod
    def read_media(self, storage_name: str, media_type: MediaType) -> bytes: ...

    @abstractmethod
    def save_media(self, storage_name: str, media_file: bytes, media_type: MediaType) -> str: ...


    @abstractmethod
    def get_storage_status(self) -> dict:...