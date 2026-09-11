from config.platform.platform_setting import PlatformSetting


class BaleSetting(PlatformSetting):
    base_url = "https://tapi.bale.ai/bot<token>/<method>"
    active = True  

    def activate(self):
        self.active = True 
    
    def deactivate(self):
        self.active= False
    
bale_setting = BaleSetting()