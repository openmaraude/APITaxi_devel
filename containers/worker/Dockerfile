FROM le.taxi/api

USER root
RUN useradd worker
RUN echo "worker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER worker
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH
ENV APITAXI_CONFIG_FILE=/settings.py

CMD ["watchmedo", "auto-restart", "--directory=/git/", "--pattern='*.py'", "--recursive", "--", "celery", "worker", "--app=APITaxi2.celery_worker.celery", "-E", "-c", "1"]
