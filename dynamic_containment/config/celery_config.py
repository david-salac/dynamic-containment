from config.setting.config import CONFIG

# Configure CELERY variables
# See: https://docs.celeryproject.org/en/stable/userguide/configuration.html
broker_url = CONFIG.CELERY_URL
result_backend = CONFIG.CELERY_URL
task_serializer = 'json'
result_serializer = 'json'
timezone = "UTC"
enable_utc = True
task_default_queue = "default"
accept_content = ['application/json']

# Enforce Celery to reserve just one task at a time
task_acks_late = True
worker_prefetch_multiplier = 1
concurrency = 1

# For unit-testing
task_always_eager = False
