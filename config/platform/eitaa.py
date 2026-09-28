from config.platform.platform_setting import PlatformSetting


class EitaaSetting(PlatformSetting):
    base_url = "https://eitaayar.ir/api/<token>/<method>"
    active = False
