from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_base_url: str = 'https://api.inchat.pp.ua:4433/'   # / в кінці не треба

settings = Settings()