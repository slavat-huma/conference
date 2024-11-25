import os

from pydantic import BaseModel


class DeepGramConfig(BaseModel):
    key: str


class ServerConfig(BaseModel):
    host: str
    port: int
    secret: str
    deepGram: DeepGramConfig

    @classmethod
    def from_env(cls):
        return cls(
            host=os.getenv("CS_HOST", "0.0.0.0"),
            port=int(os.getenv("CS_PORT", 8000)),
            secret=os.getenv("CS_SECRET"),
            deepGram=DeepGramConfig(key=os.environ.get("CS_DEEPGRAM_KEY")),
        )


SERVER_CONFIG = ServerConfig.from_env()
