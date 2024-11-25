from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/translation", tags=["translation"])


@router.get("/")
async def root():
    return "Test api."


@router.post("/audio-file-to-text")
async def audio_file_to_text():
    return "text"
