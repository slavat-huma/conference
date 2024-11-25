from typing import Annotated

from fastapi import APIRouter, File, UploadFile, Depends

from storage.adapters.di import storage_adapter
from storage.adapters.storage import StorageAdapter
from storage.use_cases import UploadFileUseCase

api = APIRouter(prefix="/api/v1/storage", tags=["storage"])


@api.post("/upload")
async def upload_file(
    file: UploadFile, adapter: Annotated[StorageAdapter, Depends(storage_adapter)]
):
    await UploadFileUseCase(adapter).execute(file)
