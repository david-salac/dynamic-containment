import os
from celery import Celery
from config import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Create celery application
CELERY_APP = Celery('dynamic-containment')

# Load Celery config file
CELERY_APP.config_from_object('config.celery_config')

# Add all tasks
CELERY_APP.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@CELERY_APP.task
def life_beat():
    """Testing task for Celery"""
    return "hello from Celery worker"
