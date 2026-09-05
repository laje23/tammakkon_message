from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerifyMismatchError

from domain.interfaces.hash_service import IHashService


class HashService(IHashService):

    def __init__(self):
        self._hasher = PasswordHasher()

    def hash(self, value: str) -> str:
        return self._hasher.hash(value)

    def verify(self, value: str, hashed_value: str) -> bool:
        try:
            return self._hasher.verify(hashed_value, value)

        except (VerifyMismatchError, InvalidHashError):
            return False
