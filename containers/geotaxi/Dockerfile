FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

RUN apt-get update && apt-get install -y \
  less \
  python3-pip \
  sudo \
  vim

RUN pip3 install virtualenv

# Create user and add in sudo
RUN useradd geotaxi
RUN echo "geotaxi ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER geotaxi
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH

WORKDIR /git/geotaxi-python

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["geotaxi", "-h", "0.0.0.0", "-p", "8080", "--redis-host", "redis", "--fluent-host", "fluentd", "--api-url", "http://api:5000/", "-v"]
