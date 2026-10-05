from config.secrets import secrets
from cryptography.fernet import Fernet, InvalidToken
from domain.interfaces import IEncription


class EncryptionService(IEncription):

    def __init__(self):

        print("ENCRYPTION INIT - 1", flush=True)

        key = secrets.encriptio_key

        print("ENCRYPTION INIT - 2", flush=True)

        print(
            "ENCRYPTION KEY TYPE:",
            type(key),
            flush=True,
        )

        print(
            "ENCRYPTION KEY LENGTH:",
            len(key) if key else 0,
            flush=True,
        )

        if not key:
            raise RuntimeError("ENCRYPTION_KEY is not set")

        print("ENCRYPTION INIT - 3", flush=True)

        encoded_key = key.encode()

        print("ENCRYPTION INIT - 4", flush=True)

        self.fernet = Fernet(encoded_key)

        print("ENCRYPTION INIT - 5", flush=True)

    def encrip(self, value: str) -> str:
        print("ENCRYPT - START", flush=True)

        encrypted = self.fernet.encrypt(value.encode())

        print("ENCRYPT - DONE", flush=True)

        return encrypted.decode()

    def decrip(self, value: str) -> str:
        print("DECRYPT - START", flush=True)

        print("DECRYPT - VALUE TYPE:", type(value), flush=True)
        print("DECRYPT - VALUE LENGTH:", len(value) if value else 0, flush=True)

        if not value:
            raise ValueError("Encrypted value is empty")

        print("DECRYPT - ENCODING START", flush=True)

        encoded_value = value.encode()

        print("DECRYPT - ENCODING DONE", flush=True)

        print("DECRYPT - FERNET DECRYPT START", flush=True)

        try:
            decrypted = self.fernet.decrypt(encoded_value)

        except InvalidToken:
            print("DECRYPT - INVALID TOKEN", flush=True)
            raise

        print("DECRYPT - FERNET DECRYPT DONE", flush=True)

        print("DECRYPT - DECODING START", flush=True)

        result = decrypted.decode()

        print("DECRYPT - DECODING DONE", flush=True)

        return result
