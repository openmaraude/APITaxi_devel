DEBUG = False
SECRET_KEY = 'super-secret'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@db/taxis'
REDIS_URL = "redis://:@redis:6379/0"
REDIS_SAVED_URL = "redis://:@redis:6379/0"
SQLALCHEMY_POOL_SIZE = 2

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = [
    'pickle',
    'application/json'
]

INFLUXDB_HOST = None

SECURITY_PASSWORD_HASH = 'plaintext'
NOW = 'time_test'
DEFAULT_MAX_RADIUS = 15*1000 #in meters
