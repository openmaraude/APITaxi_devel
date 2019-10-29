FROM le.taxi/api

USER root
RUN useradd front
RUN echo "front ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER front
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH

ENV FLASK_DEBUG=1
ENV FLASK_APP=APITaxi_front

WORKDIR /git/APITaxi_front/
