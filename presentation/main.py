from contextlib import asynccontextmanager
import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from presentation.routes import Ruotes
from infrastructure.scheduler.cron import background_scheduler


class Main:

    def __init__(self, app: FastAPI) -> None:

        self.app = app
        self.scheduler_task: asyncio.Task | None = None

        self.routes = Ruotes(app)

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                "http://localhost:5173",
                "http://127.0.0.1:5173",
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.routes.defination_routes()

        self.app.router.lifespan_context = self.lifespan

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):

        self.scheduler_task = asyncio.create_task(background_scheduler.start())

        yield

        if self.scheduler_task:

            self.scheduler_task.cancel()

            try:
                await self.scheduler_task
            except asyncio.CancelledError:
                pass


main = Main(FastAPI())

app = main.app
