import uvicorn
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI

load_dotenv(find_dotenv("dev.env"))

import translation
from server.config import SERVER_CONFIG

app = FastAPI()
app.include_router(
    translation.router, prefix="/api/v1/translation", tags=["translation"]
)
app.include_router(translation.view_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=SERVER_CONFIG.host,
        port=SERVER_CONFIG.port,
    )
