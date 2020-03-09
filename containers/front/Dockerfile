FROM le.taxi/api

USER root

# Install nodejs
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get install -y nodejs

# Create front user
RUN useradd front
RUN echo "front ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER front
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH

ENV FLASK_DEBUG=1
ENV FLASK_APP=APITaxi_front

WORKDIR /git/APITaxi_front/
