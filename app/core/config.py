from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openrouter_api_key: str= Field(..., env="OPENROUTER_API_KEY")
    openrouter_model: str= Field(..., env="OPENROUTER_MODEL")
    debug: bool= Field(..., env="DEBUG")

    class Config:
        env_file = ".env"

settings = Settings() 