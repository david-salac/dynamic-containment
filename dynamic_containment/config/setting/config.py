import os

from config.setting.base_config import BaseConfig
from config.setting.local import LocalConfig
from config.setting.production import ProductionConfig


environment = os.getenv('ENVIRONMENT', "LOCAL")

CONFIG: type[BaseConfig] = LocalConfig
if environment == "PRODUCTION":
    CONFIG = ProductionConfig
