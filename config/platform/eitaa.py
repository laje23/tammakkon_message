from config.platform.platform_setting import PlatformSetting


class EitaaSetting(PlatformSetting):
    base_url = "https://eitaayar.ir/api/<token>/<method>"
    active = True

    def activate(self):
        self.active = True 
    
    def deactivate(self):
        self.active= False
    
eitaa_setting = EitaaSetting()