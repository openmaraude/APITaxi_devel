#!/bin/sh

# If the directory /venv/ is empty, fill it with a new virtualenv. /venv can be
# mounted as a docker volume to persist packages installation.
sudo -E find /venv/ -maxdepth 0 -empty -exec virtualenv /venv \;

. /venv/bin/activate

sudo -E /venv/bin/pip install flower tox

for proj in APITaxi_utils APITaxi_models APITaxi APITaxi_front;
do
    test -d "/git/${proj}" && sudo -E /venv/bin/pip install -e "/git/${proj}"
done

# Execute Docker CMD
exec "$@"
