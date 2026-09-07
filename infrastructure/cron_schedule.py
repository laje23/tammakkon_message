from typing import Callable
from asyncio import sleep

class CronSchedule:
    async def run(self, proccess_func:Callable):
        while True :
            proccess_func()
            await sleep(300)