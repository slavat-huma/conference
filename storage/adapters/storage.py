from abc import ABC, abstractmethod
from typing import BinaryIO

from common.utils import SingletonABCMeta


class StorageAdapter(ABC, metaclass=SingletonABCMeta):
    config = None

    @abstractmethod
    async def upload_file(self, file_name: str, data: BinaryIO, length: int):
        raise NotImplementedError
