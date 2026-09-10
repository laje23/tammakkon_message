from config.setting import settings
from cryptography.fernet import Fernet


class EncryptionService:

    def __init__(self):
        key = settings.encriptio_key
        if not key:
            raise RuntimeError("ENCRYPTION_KEY is not set")
        self.fernet = Fernet(key.encode())

    def encrypt(self, value: str) -> str:
        encrypted = self.fernet.encrypt(value.encode())
        return encrypted.decode()

    def decrypt(self, value: str) -> str:
        decrypted = self.fernet.decrypt(value.encode())
        return decrypted.decode()