from config.setting.base_config import BaseConfig


class LocalConfig(BaseConfig):
    """Configuration for local stack"""
    DJANGO_DEBUG_MODE: bool = True
    DJANGO_SECRET_KEY: str = \
        'django-insecure-+t*s*=b2#=e9zwzhj-e=w4g*940py=+85c3@lq**ly45a8c2%+'
    DJANGO_ALLOWED_HOSTS: list[str] = ['127.0.0.1', 'localhost', '0.0.0.0']

    DATABASE_NAME: str = 'postgres'
    DATABASE_USER: str = 'postgres'
    DATABASE_PASSWORD: str = 'postgres'
    DATABASE_HOST: str = 'db'
    DATABASE_PORT: str = '5432'

    REDIS_HOSTNAME: str = "redis"
    REDIS_PASSWORD: str = "nxaaLkv8"
    REDIS_PORT: int = 6389
    REDIS_DB_NUMBER: int = 1
