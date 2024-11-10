import os

from pydantic import BaseModel


class DeepGramConfig(BaseModel):
    key: str


class ServerConfig(BaseModel):
    host: str
    port: int
    deepGram: DeepGramConfig

    @classmethod
    def from_env(cls):
        return cls(
            host=os.environ.get("CS_HOST", "0.0.0.0"),
            port=int(os.environ.get("CS_PORT", 8000)),
            deepGram=DeepGramConfig(key=os.environ.get("CS_DEEP_GRAM_KEY")),
        )


SERVER_CONFIG = ServerConfig.from_env()
