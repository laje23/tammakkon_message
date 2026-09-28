from abc import ABC, abstractmethod


class IStorageService(ABC):

    @abstractmethod
    def read_media(self, storge_name: str) -> bytes: ...

    @abstractmethod
    def save_media(self, storage_name: str, file: bytes) -> None: ...
