from threading import Lock
from typing import Optional

from url_shortener.storage import Storage
from url_shortener.dto import User


class Logic:
    def __init__(self, storage: Storage):
        super().__init__()
        self._storage: Storage = storage
        self._check_and_write_lock: Lock = Lock()

    def get_example(self, key: str) -> Optional[str]:
        return self._storage.read(key)

    def save_example_if_not_exists(self, key: str, value: str) -> bool:
        """ Tries to save value at given key.
        Fails if key already has value in the storage.
        Returns True if saving value was successful, otherwise False
        """
        # Acquire lock, so that we do not get ourselves into the data race
        with self._check_and_write_lock:
            existing = self._storage.read(key)
            if existing is not None:
                return False

            self._storage.write(key, value)
            return True

    def find_user_by_token(self, token: str) -> Optional[User]:
        # TODO: implement actual checking logic
        if token.strip():
            return User(email='implementme@example.com')
        return None
