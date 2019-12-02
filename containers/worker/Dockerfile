FROM le.taxi/api

USER root
RUN useradd worker
RUN echo "worker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER worker
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH
ENV APITAXI_CONFIG_FILE=/settings.py

CMD ["celery", "worker", "--app=celery_worker.celery", "-Q", "send_hail_time_test", "-E"]
