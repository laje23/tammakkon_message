from domain.interfaces import IMediaService


class MediaService(IMediaService):

    def read(self, storage_name: str) -> bytes:
        with open(storage_name, "rb") as file:
            return file.read()

    def save(
        self,
        storage_name: str,
        media_file: bytes
    ):
        with open(storage_name, "wb") as file:
            file.write(media_file)