DEBUG = True
ENV = 'DEV'
PORT = 80
SECRET_KEY = 'super-secret'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@db/taxis'

REDIS_URL = "redis://:@redis:6379/0"
REDIS_SAVED_URL = "redis://:@redis:6379/0"


REDIS_GEOINDEX = 'geoindex_2'
REDIS_GEOINDEX_ID = 'geoindex'
REDIS_TIMESTAMPS = 'timestamps'
REDIS_TIMESTAMPS_ID = 'timestamps_id'
REDIS_NOT_AVAILABLE = 'not_available'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'pepper'
UPLOADED_IMAGES_DEST = 'uploads'

UPLOADED_DOCUMENTS_DEST = 'uploads'
UPLOADED_DOCUMENTS_URL = '/documents/<path:filename>'

SLACK_API_KEY = None

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = [
    'pickle',
    'application/json'
]

from celery.schedules import crontab

#List of tuples of the form
# (frequency in minute, kwargs) where kwargs in passed to crontab
STORE_TAXIS_FREQUENCIES = [
    (1, {'minute': '*/1'}),
    (60, {'minute': 0, 'hour': '*/1'}),
    (24 * 60, {'minute': 0, 'hour': 0})
]

CELERYBEAT_SCHEDULE = dict([
    ('clean_timestamps', {
        'task': 'clean_geoindex_timestamps',
        'schedule': crontab(minute='*/1'),
    })
])

for frequency, cron_kwargs in STORE_TAXIS_FREQUENCIES:
    CELERYBEAT_SCHEDULE['store_active_taxis_every_{}'.format(frequency)] =  {
        'task': 'store_active_taxis',
        'schedule': crontab(**cron_kwargs),
        'args': [frequency]
    }

INFLUXDB_HOST = 'influxdb'
INFLUXDB_PORT = 8086
INFLUXDB_USER = ''
INFLUXDB_PASSWORD = ''
INFLUXDB_TAXIS_DB = 'taxis'
NOW = 'now'
LIMITED_ZONE = None
SQLALCHEMY_TRACK_MODIFICATIONS = True

SLACK_CHANNEL = "#taxis-internal"

# Set to False until the issue is fixed: https://github.com/noirbizarre/flask-restplus/issues/693
PROPAGATE_EXCEPTIONS = False
