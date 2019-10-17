FROM debian

RUN apt-get update && apt-get install -y \
  git \
  less \
  libffi-dev \
  libgeos-dev \
  libpq-dev \
  python3-pip \
  vim

RUN pip3 install virtualenv

WORKDIR /git/APITaxi

ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

ENV APITAXI_CONFIG_FILE=/settings.py
ENV FLASK_DEBUG=1
ENV FLASK_APP=APITaxi
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
