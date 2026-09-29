import os
from dotenv import load_dotenv

load_dotenv()


class _Secrets:

    @property
    def database_url(self) -> str:
        value = os.getenv("DATABASE_URL")

        if not value:
            raise RuntimeError("DATABASE_URL is not set")

        return value

    @property
    def debug(self) -> bool:
        return os.getenv("DEBUG", "False").lower() == "true"

    @property
    def encriptio_key(self) -> str:
        value = os.getenv("ENCRIPTION_KEY")

        if not value:
            raise RuntimeError("ENCRIPTION_KEY is not set")
        return value
    


secrets = _Secrets()
