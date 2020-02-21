#!/bin/sh

# If the directory /venv/ is empty, fill it with a new virtualenv. /venv can be
# mounted as a docker volume to persist packages installation.
sudo -E find /venv/ -maxdepth 0 -empty -exec virtualenv /venv \;

. /venv/bin/activate

sudo -E /venv/bin/pip install tox
sudo -E /venv/bin/pip install inotify
sudo -E /venv/bin/pip install -e "/git/geotaxi-python"


# Execute Docker CMD
exec "$@"