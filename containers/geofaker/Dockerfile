FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

RUN apt-get update && apt-get install -y \
  git \
  less \
  libffi-dev \
  libgeos-dev \
  libpq-dev \
  python3-pip \
  sudo \
  vim

RUN pip3 install virtualenv

WORKDIR /git/geofaker

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

# Create user and add in sudo
RUN useradd geofaker
RUN echo "geofaker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER geofaker
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH

# Fake random taxis file generated for development purpose. API keys are not
# valid, so geotaxi should not be configured to verify them.
COPY taxis_file.csv /

CMD ["geofaker", "--geotaxi-addr", "geotaxi", "/taxis_file.csv", "paris-small.gpx"]
