from config.secrets import secrets
from cryptography.fernet import Fernet
from domain.interfaces import IEncription


class EncryptionService(IEncription):

    def __init__(self):
        key = secrets.encriptio_key
        if not key:
            raise RuntimeError("ENCRYPTION_KEY is not set")
        self.fernet = Fernet(key.encode())

    def encrip(self, value: str) -> str:
        encrypted = self.fernet.encrypt(value.encode())
        return encrypted.decode()

    def decrip(self, value: str) -> str:
        decrypted = self.fernet.decrypt(value.encode())
        return decrypted.decode()
