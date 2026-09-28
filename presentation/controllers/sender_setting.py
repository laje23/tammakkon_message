from config import SendConfigs


class SenderSettingController:

    def get_setting(self):
        return {
            "time_out": SendConfigs.time_out,
            "max_try": SendConfigs.max_try,
            "use_proxy": SendConfigs.use_proxy,
        }

    def update_setting(self, data):

        settings = {
            "time_out": data.time_out,
            "max_try": data.max_try,
            "use_proxy": data.use_proxy,
        }

        for attribute, value in settings.items():
            if value is not None:
                setattr(SendConfigs, attribute, value)

        return {
            "success": True,
            "message": "تنظیمات ارسال با موفقیت ذخیره شد",
        }
