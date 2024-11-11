from abc import ABC, abstractmethod


class StorageAdapter(ABC):

    @abstractmethod
    async def upload_file(self):
        raise NotImplementedError
