from typing import Callable
from asyncio import sleep
from inspect import iscoroutinefunction

class BackgroundScheduler:

    def __init__(self, jobs: dict[Callable, int]) -> None:

        self.jobs = {}

        for func, set_time in jobs.items():

            if set_time <= 0:
                raise ValueError("Job interval must be greater than zero")

            self.jobs[func] = {
                "counter": 0,
                "set_time": set_time
            }

    async def start(self, sleep_time: int = 60):

        while True:

            for func, time_data in self.jobs.items():

                time_data["counter"] += 1

                if time_data["counter"] >= time_data["set_time"]:

                    time_data["counter"] = 0

                    if iscoroutinefunction(func):
                        await func()
                    else:
                        func()

            await sleep(sleep_time)