from httpx import post
from config import SendConfigs


def send_post(data):
    response = post(**data, timeout=SendConfigs.time_out)
    response.raise_for_status()
    return response.json()
