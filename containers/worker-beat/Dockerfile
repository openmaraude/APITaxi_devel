FROM le.taxi/worker

CMD ["watchmedo", "auto-restart", "--directory=/git/", "--pattern='*.py'", "--recursive", "--", "celery", "beat", "--app=APITaxi2.celery_worker.celery", "-s", "/tmp/celerybeat-schedule"]
