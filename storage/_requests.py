from io import IOBase

from pydantic import BaseModel


class UploadFileRequestObject(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    file_name: str
    length: int
    data: IOBase
