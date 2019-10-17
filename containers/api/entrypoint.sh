#!/bin/sh

# If the directory /venv/ is empty, fill it with a new virtualenv. /venv can be
# mounted as a docker volume to persist packages installation.
find /venv/ -maxdepth 0 -empty -exec virtualenv /venv \;

pip3 install -e /git/APITaxi_utils
pip3 install -e /git/APITaxi_models
pip3 install -e /git/APITaxi

# Execute Docker CMD
exec "$@"
