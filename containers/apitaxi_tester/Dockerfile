FROM debian

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

WORKDIR /git/APITaxi_tester

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

# Create user and add in sudo
RUN useradd api
RUN echo "api ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER api
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH

ENV FLASK_DEBUG=1
ENV FLASK_APP=APITaxi_tester.front:create_app
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
