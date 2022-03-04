"""
This module implements json database for handling collections and persists it in a json files.
"""
from typing import Dict, List

from .collection import JsonCollection

class JsonDatabase:
    """
        Represents a json database.
    """
    def __init__(self, path: str, names: List[str]) -> None:
        """
            Constructor json database.

            :param path: The path from data collections
            :param names: List of collection names
        """
        self._path = path
        self._collections: Dict[str, JsonCollection] = {
            name: JsonCollection(name, self._path) for name in names
        }
        self._opened = True

    def __enter__(self):
        """
            When the JsonDatabase as a context manager
        """
        return self

    def __exit__(self, *args):
        """
            Close database when leaving a context.
        """
        if self._opened:
            self.close()

    @property
    def collections(self) -> Dict[str, JsonCollection]:
        """
        Get all collections in database.
        """
        return self._collections

    def collection(self, name: str) -> JsonCollection:
        """
            Get access to a specific collection.

            :param name: The name of the collection.
        """
        if name in self._collections:
            return self._collections[name]

        self._collections[name] = JsonCollection(self._path, name)
        self._opened = True
        return self._collections[name]

    def close(self) -> None:
        """
            Close the database.
        """
        self._opened = False

        for name in self._collections:
            self._collections[name].storage.close()
