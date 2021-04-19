FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

RUN apt-get update && apt-get install -y \
  python3-pip \
  redis-tools \
  sudo \
  postgresql-client

ENV LC_ALL=C.UTF-8

RUN pip3 install tox

RUN useradd api
RUN echo "api ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH
ENV HOME=/tmp

ENV FLASK_APP minimal_operateur_server.api:create_app
env API_SETTINGS=/settings.py
env FLASK_DEBUG=1

USER api
WORKDIR /git/minimal_operateur_server

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["flask", "run", "--host", "0.0.0.0"]
