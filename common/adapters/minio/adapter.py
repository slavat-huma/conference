import os

from minio import Minio
from pydantic import BaseModel

from common.adapters.storage import StorageAdapter
from common.utils import SingletonMeta


class MinioConfig(BaseModel):
    url: str
    base_url: str
    access_key: str
    secret_key: str
    secure: bool

    @classmethod
    def from_env(cls):
        return cls(
            url=os.getenv("CS_MINIO_URL"),
            base_url=os.getenv("CS_MINIO_BASE_URL"),
            access_key=os.getenv("CS_MINIO_ACCESS_KEY"),
            secret_key=os.getenv("CS_MINIO_SECRET_KEY"),
            secure=os.getenv("CS_MINIO_SECURE", False),
        )


class MinioStorageAdapter(StorageAdapter, metaclass=SingletonMeta):
    def __init__(self):
        self.config = MinioConfig.from_env()
        self.client = Minio(
            self.config.url,
            access_key=self.config.access_key,
            secret_key=self.config.secret_key,
            secure=self.config.secure,
        )

    async def upload_file(self):
        pass
