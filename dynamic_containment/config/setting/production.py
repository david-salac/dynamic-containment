import os
import json
from config.setting.base_config import BaseConfig


class ProductionConfig(BaseConfig):
    """Configuration for local stack"""
    DJANGO_DEBUG_MODE: bool = False
    DJANGO_SECRET_KEY: str = os.getenv('DJANGO_SECRET_KEY')
    # Following pass in the form of string: '["example.com", "x.example.com"]'
    DJANGO_ALLOWED_HOSTS: list[str] = \
        json.loads(os.getenv('ALLOWED_HOSTS', '[]'))

    DATABASE_NAME: str = os.getenv('DATABASE_NAME')
    DATABASE_USER: str = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST: str = os.getenv('DATABASE_HOST')
    DATABASE_PORT: str = os.getenv('DATABASE_PORT')

    REDIS_HOSTNAME: str = os.getenv('REDIS_HOSTNAME')
    REDIS_PASSWORD: str = os.getenv('REDIS_PASSWORD')
    REDIS_PORT: int = int(os.getenv('REDIS_PORT', 0))
    REDIS_DB_NUMBER: int = int(os.getenv('REDIS_DB_NUMBER', 0))
