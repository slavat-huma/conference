from fastapi import APIRouter

from server.config import SERVER_CONFIG

router = APIRouter()


@router.get("/")
async def root():
    return {f"Test api. Test value: {SERVER_CONFIG.deepGram.key}"}
