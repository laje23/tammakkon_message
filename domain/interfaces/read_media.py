from abc import ABC, abstractmethod


class IMediaService(ABC):

    @abstractmethod
    def read(self, storge_name: str) -> bytes: ...

    @abstractmethod
    def save(self, storage_name: str, file: bytes) -> None:
        ...