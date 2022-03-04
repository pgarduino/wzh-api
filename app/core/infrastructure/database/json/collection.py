"""
This module implements json collections for handling documents and persists it in a json files.
"""
from typing import Dict, List, Callable, Optional

from .storage import JsonStorage

class JsonCollection:
    """
        Represents a json collection.
    """
    def __init__(self, name: str, path: str) -> None:
        """
            Constructor a json collection.

            :param name: The collection name
            :param path: The path from data collection
        """
        filename = "{}/{}.json".format(path, name)
        self._storage = JsonStorage(filename)

    @property
    def storage(self) -> JsonStorage:
        """
            storage of json collection.
        """
        return self._storage

    def _read(self):
        """
            read documents of json collection.
        """
        documents = self._storage.read()
        if documents is None:
            return []
        return documents

    def all(self) -> List[Dict]:
        """
            get all documents of json collection.
        """
        return self._read()

    def search(self, callback: Callable) -> List[Dict]:
        """
            search documents of json collection by callback.

            :param callback: The callback to filter documents.
        """
        documents = self._read()
        return list(filter(callback, documents))

    def get(self, _id: int, pk: str = 'id') -> Optional[Dict]:
        """
            get documents of json collection by id.

            :param _id: The identifier of documents
            :param pk: The name of key identifier of documents
        """
        documents = self._read()
        documents_map = {document[pk]: document for document in documents}
        if _id not in documents_map:
            return None
        return documents_map[_id]
