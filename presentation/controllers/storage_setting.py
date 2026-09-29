from config import StorageConfig
from infrastructure.dependency_Injection import container


class StorageSettingController:

    container = container

    def get_storage_setting(self):
        setting_dict = self.container.storage_service.get_storage_status()
        return {
            "photo_folder": StorageConfig.photo_folder_name,
            "audio_folder": StorageConfig.audio_folder_name,
            "video_folder": StorageConfig.video_folder_name,
            "document_folder": StorageConfig.document_folder_name,
            "storage_capacity_mb": StorageConfig.storage_capacity_mb,
            **setting_dict,
        }

    def update_setting(self, data):
        update_dict = {
            "photo_folder_name": data.photo,
            "audio_folder_name": data.audio,
            "video_folder_name": data.video,
            "document_folder_name": data.document,
            "storage_capacity_mb": data.storage_capacity_mb,
        }

        for key, value in update_dict.items():
            if value is not None:
                setattr(StorageConfig, key, value)

        return {
            "success": True,
            "message": "تنظیمات ذخیره شد",
        }