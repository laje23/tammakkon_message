from pathlib import Path
from uuid import uuid4

from config.storage import StorageConfig
from domain.interfaces import IStorageService
from domain.types import MediaType
from domain.exeptions import InvalidStateError

class StorageService(IStorageService):
    storage_warning_active = False

    def __init__(self):
        self.root_path = Path(StorageConfig.storage_root_path)
        self._initialize_storage()

    def _initialize_storage(self) -> None:
        self.root_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        for folder in self._get_media_folders().values():
            (self.root_path / folder).mkdir(
                parents=True,
                exist_ok=True,
            )

    def _get_directories_size(self) -> dict[MediaType, int]:
        return {
            media_type: sum(
                file.stat().st_size
                for file in (self.root_path / folder).rglob("*")
                if file.is_file()
            )
            for media_type, folder in self._get_media_folders().items()
        }

    def _get_media_folders(self) -> dict[MediaType, str]:
        return {
            MediaType.PHOTO: StorageConfig.photo_folder_name,
            MediaType.AUDIO: StorageConfig.audio_folder_name,
            MediaType.VIDEO: StorageConfig.video_folder_name,
            MediaType.DOCUMENT: StorageConfig.document_folder_name,
        }

    def _get_media_folder(self, media_type: MediaType) -> str:
        folder = self._get_media_folders().get(media_type)

        if folder is None:
            raise ValueError(
                f"Unsupported media type: {media_type}"
            )

        return folder

    def _generate_storage_name(self, original_name: str) -> str:
        extension = Path(original_name).suffix

        return f"{uuid4().hex}{extension}"

    def has_enough_space(self, file_size: int) -> bool:
        """
        Checks whether there is enough storage space for a new file.
        """

        if file_size < 0:
            raise ValueError("File size cannot be negative")

        size_data = self._get_directories_size()

        total_used_size = sum(size_data.values())

        max_capacity = StorageConfig.storage_capacity_mb * 1024 * 1024

        remaining_space = max_capacity - total_used_size

        return remaining_space >= file_size

    def save_media(
        self,
        media_file: bytes,
        media_type: MediaType,
        storage_name: str,
    ) -> str:

        self._initialize_storage()

        file_size = len(media_file)

        if not self.has_enough_space(file_size):
            raise InvalidStateError("Not enough storage space")

        folder = self._get_media_folder(media_type)

        stored_name = self._generate_storage_name(storage_name)

        storage_path = self.root_path / folder / stored_name

        with open(storage_path, "wb") as file:
            file.write(media_file)

        return stored_name

    def read_media(
        self,
        storage_name: str,
        media_type: MediaType,
    ) -> bytes:

        folder = self._get_media_folder(media_type)

        storage_path = self.root_path / folder / storage_name

        with open(storage_path, "rb") as file:
            return file.read()

    def get_storage_status(self) -> dict:
        sizes = self._get_directories_size()

        used_size = sum(sizes.values())
        capacity = StorageConfig.storage_capacity_mb * 1_000_000

        return {
            "used_size": used_size,
            "capacity": capacity,
            "used_percentage": (
                (used_size / capacity) * 100
                if capacity > 0 else 0
            ),
            "photo_size": sizes.get(MediaType.PHOTO, 0),
            "audio_size": sizes.get(MediaType.AUDIO, 0),
            "video_size": sizes.get(MediaType.VIDEO, 0),
            "document_size": sizes.get(MediaType.DOCUMENT, 0),
        }
        
    def check_folders_capacity(self) -> float:
        size_data = self._get_directories_size()
        total = sum(size_data.values())

        max_capacity = StorageConfig.storage_capacity_mb * 1024 * 1024

        return total / max_capacity * 100