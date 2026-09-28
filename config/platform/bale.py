from config.platform.platform_setting import PlatformSetting


class BaleSetting(PlatformSetting):
    base_url = "https://tapi.bale.ai/bot<token>/<method>"
    active = False
