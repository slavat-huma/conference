import uvicorn
from fastapi import FastAPI

import translation
from server.config import SERVER_CONFIG

app = FastAPI()
app.include_router(
    translation.router, prefix="/api/v1/translation", tags=["translation"]
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=SERVER_CONFIG.host,
        port=SERVER_CONFIG.port,
    )
