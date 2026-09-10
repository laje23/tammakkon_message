from infrastructure.platforms.senders import *
from domain.types import PlatformType
from domain.interfaces import ISender , IGetPlatform

class GetPlatform(IGetPlatform):
    platform_dict={
        PlatformType.BALE: BaleSender(), 
        PlatformType.EITAA : EitaaSender() ,
        PlatformType.ROBIKA : RobikaSender()
    }
    
    def get_platform(self, type: PlatformType )->ISender :
        return self.platform_dict[type]
    