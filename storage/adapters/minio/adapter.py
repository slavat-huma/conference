import os
from typing import BinaryIO

from minio import Minio
from pydantic import BaseModel

from storage.adapters.storage import StorageAdapter


class MinioConfig(BaseModel):
    url: str
    base_url: str
    access_key: str
    secret_key: str
    secure: bool
    bucket: str

    @classmethod
    def from_env(cls):
        return cls(
            url=os.getenv("CS_MINIO_URL"),
            base_url=os.getenv("CS_MINIO_BASE_URL"),
            access_key=os.getenv("CS_MINIO_ACCESS_KEY"),
            secret_key=os.getenv("CS_MINIO_SECRET_KEY"),
            secure=os.getenv("CS_MINIO_SECURE", False),
            bucket=os.getenv("CS_BUCKET_NAME", False),
        )


class MinioStorageAdapter(StorageAdapter):
    def __init__(self):
        self.config = MinioConfig.from_env()
        self.client = Minio(
            self.config.url,
            access_key=self.config.access_key,
            secret_key=self.config.secret_key,
            secure=self.config.secure,
        )

    async def upload_file(self, file_name: str, data: BinaryIO, length: int):
        self.client.put_object(self.config.bucket, file_name, data, length)
