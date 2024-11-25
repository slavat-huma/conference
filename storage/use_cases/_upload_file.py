from common.use_case import UseCase
from storage.adapters.storage import StorageAdapter


class UploadFileUseCase(UseCase):
    def __init__(self, adapter: StorageAdapter):
        super().__init__()
        self.adapter = adapter

    async def process_request(self):
        print(self.adapter.config)
