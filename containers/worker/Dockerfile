FROM le.taxi/api

USER root
RUN useradd worker
RUN echo "worker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER worker
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH
ENV APITAXI_CONFIG_FILE=/settings.py

# If we use the square bracket CMD style, process doesn't auto-reload on code change.
# The simple CMD format is used on purpose, until we understand why CMD [...] doesn't work.
CMD watchmedo auto-restart --directory=/git/ --pattern='*.py' --recursive -- celery --app=APITaxi2.celery_worker.celery worker -E -c 1
