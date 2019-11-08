# This Dockerfile is more or less a copy of geotaxi/Dockerfile, but it adds a
# fancy entrypoint to relaunch the server on code change.

FROM debian:stretch

RUN apt-get update && apt-get install -y \
    autoconf-archive \
    automake \
    autoconf \
    build-essential \
    check \
    libspatialindex-dev \
    libhiredis-dev \
    libgcrypt11-dev \
    libcurl4-openssl-dev \
    wait-for-it

RUN apt-get install -y \
    inotify-tools \
    procps

WORKDIR /geotaxi
COPY entrypoint.sh /

ENTRYPOINT /entrypoint.sh
