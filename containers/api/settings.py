SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@db/taxis'

REDIS_URL = "redis://:@redis:6379/0"

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

INFLUXDB_HOST = 'influxdb'
