from config.platform.platform_setting import PlatformSetting


class RobikaSetting(PlatformSetting):
    base_url = "https://botapi.rubika.ir/v3/<token>/<method>"
    active = True 
    
    def activate(self):
        self.active = True 
    
    def deactivate(self):
        self.active= False
    
robika_setting = RobikaSetting()