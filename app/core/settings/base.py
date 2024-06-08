import os
from enum import Enum
from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    local: str = "local"
    test: str = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes(os.getenv("ENV", "dev"))

    class Config:
        extra = "allow"
        env_file = ".env"
