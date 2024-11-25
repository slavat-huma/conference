from storage.adapters.minio.adapter import MinioStorageAdapter
from storage.adapters.storage import StorageAdapter


async def storage_adapter() -> StorageAdapter:
    return MinioStorageAdapter()
