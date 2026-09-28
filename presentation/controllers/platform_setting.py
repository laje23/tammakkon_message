from config.platform import (
    PlatformSetting,
    BaleSetting,
    EitaaSetting,
    RobikaSetting,
)


class PlatformSettingController:

    def get_setting(self):
        return {
            "platforms_setting": {
                "limit_character": PlatformSetting.limit_character,
                "limit_file_size": PlatformSetting.limit_file_size,
            },
            "bale": {
                "base_url": BaleSetting.base_url,
                "status": BaleSetting.active,
            },
            "eitaa": {
                "base_url": EitaaSetting.base_url,
                "status": EitaaSetting.active,
            },
            "robika": {
                "base_url": RobikaSetting.base_url,
                "status": RobikaSetting.active,
            },
        }

    def update_setting(self, data):
        settings = {
            PlatformSetting: {
                "limit_character": data.limit_character,
                "limit_file_size": data.limit_file_size,
            },
            BaleSetting: {
                "base_url": data.bale_base_url,
                "active": data.bale_active,
            },
            EitaaSetting: {
                "base_url": data.eitaa_base_url,
                "active": data.eitaa_active,
            },
            RobikaSetting: {
                "base_url": data.robika_base_url,
                "active": data.robika_active,
            },
        }

        for setting_class, values in settings.items():
            for attribute, value in values.items():
                if value is not None:
                    setattr(setting_class, attribute, value)

        return {
            "success": True,
            "message": "تنظیمات پلتفرم ذخیره شد",
        }