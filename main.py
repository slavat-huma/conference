import uvicorn
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI

load_dotenv(find_dotenv("dev.env"))

import auth
import translation
from storage import storage_api
from server.config import SERVER_CONFIG

app = FastAPI()
app.include_router(auth.api)
app.include_router(translation.router)
app.include_router(storage_api)
app.include_router(translation.view_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=SERVER_CONFIG.host,
        port=SERVER_CONFIG.port,
    )
