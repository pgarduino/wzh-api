"""
This module implements json storage for store data in a file.
"""

import json
import os
from typing import Dict, Any, Optional, List

class JsonStorage:
    """
        Represents a json storage.
    """
    def __init__(self, filename: str) -> None:
        """
            Constructor a json storage.

            :param filename: The file name
        """
        self._handle = open(filename, mode='r+')

    def close(self) -> None:
        """
            Close open json file.
        """
        self._handle.close()

    def read(self) -> Optional[List[Dict[str, Any]]]:
        """
            Read json file.
        """
        self._handle.seek(0, os.SEEK_END)
        size = self._handle.tell()
        if not size:
            return None
        self._handle.seek(0)
        return json.load(self._handle)
