from common.use_case import UseCase
from storage import UploadFileRequestObject
from storage.adapters.storage import StorageAdapter


class UploadFileUseCase(UseCase):
    request_object: UploadFileRequestObject

    def __init__(self, adapter: StorageAdapter):
        super().__init__()
        self.adapter = adapter

    async def process_request(self, req_obj: UploadFileRequestObject):
        await self.adapter.upload_file(req_obj.file_name, req_obj.data, req_obj.length)
