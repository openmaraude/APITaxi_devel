INTEGRATION_ENABLED = True
INTEGRATION_ACCOUNT_EMAIL = 'neotaxi'

SECRET_KEY = 'super-secret'
SECURITY_PASSWORD_SALT = 'pepper'

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@db/taxis'

REDIS_URL = "redis://:@redis:6379/0"

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

INFLUXDB_HOST = 'influxdb'
