from abc import ABC, abstractmethod

from common.utils import SingletonABCMeta


class StorageAdapter(ABC, metaclass=SingletonABCMeta):
    config = None

    @abstractmethod
    async def upload_file(self):
        raise NotImplementedError