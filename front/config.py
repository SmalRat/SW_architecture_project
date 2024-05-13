from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    backend_url_guest: str
    backend_url_admin: str
    reservation_url: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
