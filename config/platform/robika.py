from config.platform.platform_setting import PlatformSetting


class RobikaSetting(PlatformSetting):
    base_url = "https://botapi.rubika.ir/v3/<token>/<method>"
    active = False
