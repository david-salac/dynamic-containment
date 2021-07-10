from config.setting.utils import classproperty


class BaseConfig(object):
    """Base class for app configuration"""
    # Django configuration
    DJANGO_DEBUG_MODE: bool
    DJANGO_SECRET_KEY: str
    DJANGO_ALLOWED_HOSTS: list[str]

    # Postgres configuration
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str

    # Configuration for National Grid ESO Tender
    NGE_BASE_URL: str = \
        "https://data.nationalgrideso.com/api/3/action/datastore_search"
    # Type of data (based on API definition)
    NGE_RESOURCE_ID: str = "e3e44433-7614-4c8c-9cbc-7808994d3a72"
    # The following organization is used as a default one for
    #   "Agent/Applicant" field in the query:
    NGE_DEFAULT_ORGANIZATON: str = "Habitat Energy Limited"

    # Redis
    REDIS_HOSTNAME: str
    REDIS_PASSWORD: str
    REDIS_PORT: int
    REDIS_DB_NUMBER: int

    @classproperty
    def CELERY_URL(cls) -> str:
        """Generate Celery connection URL"""
        return f"redis://:{cls.REDIS_PASSWORD}@{cls.REDIS_HOSTNAME}:" \
               f"{cls.REDIS_PORT}/{cls.REDIS_DB_NUMBER}"
