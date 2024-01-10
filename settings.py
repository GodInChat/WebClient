from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_base_url: str = 'http://127.0.0.1:8000'   # / в кінці не треба

settings = Settings()