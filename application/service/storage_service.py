from domain.interfaces import IStorageService


class StorageService(IStorageService):

    def read_media(self, storage_name: str) -> bytes:
        with open(storage_name, "rb") as file:
            return file.read()

    def save_media(self, storage_name: str, media_file: bytes):
        with open(storage_name, "wb") as file:
            file.write(media_file)
