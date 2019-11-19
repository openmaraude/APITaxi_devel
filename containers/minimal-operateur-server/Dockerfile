FROM debian

RUN apt-get update && apt-get install -y \
  sudo \
  python3-pip

RUN pip3 install virtualenv

WORKDIR /git/minimal_operateur_server

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

# Create user and add in sudo
RUN useradd api
RUN echo "api ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER api
ENV VIRTUAL_ENV=/venv
ENV PATH=/venv/bin/:$PATH

ENV FLASK_DEBUG=1
ENV FLASK_APP=minimal_operateur_server.api
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
