FROM le.taxi/worker

# If we use the square bracket CMD style, process doesn't auto-reload on code change.
# The simple CMD format is used on purpose, until we understand why CMD [...] doesn't work.
CMD watchmedo auto-restart --directory=/git/ --pattern='*.py' --recursive -- celery beat --app=APITaxi2.celery_worker.celery -s /tmp/celerybeat-schedule --pidfile /tmp/celerybeat.pid
