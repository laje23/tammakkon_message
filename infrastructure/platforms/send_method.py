from httpx import post
from config.platform import PlatformSetting

def send_post(data):
    response =post(**data , timeout= PlatformSetting.time_out)
    response.raise_for_status()
    return response.json()