#!/bin/sh

# If the directory /venv/ is empty, fill it with a new virtualenv. /venv can be
# mounted as a docker volume to persist packages installation.
sudo -E find /venv/ -maxdepth 0 -empty -exec virtualenv /venv \;

. /venv/bin/activate

sudo -E /venv/bin/pip install tox watchdog[watchmedo] pytest flake8 pylint

for d in /git/*;
do
    sudo -E /venv/bin/pip install -e "$d"
done

while true;
do
    API_KEY=$(psql -h db -U postgres taxis -t -c "SELECT apikey FROM \"user\" WHERE email = 'neotaxi'" | xargs)

    if [ "$API_KEY" ];
    then
        break
    fi

    echo "Attempt to SELECT of user 'neotaxi' failed. Retry in a few seconds. Check the db container is up, and the user exists." >&2
    sleep 3
done

sudo touch "$API_SETTINGS"
sudo chown api:api "$API_SETTINGS"

cat<<EOF > "$API_SETTINGS"
RQ_REDIS_URL = 'redis://redis:6379/0'
API_TAXI_URL = 'http://api:5000'
API_TAXI_KEY = '${API_KEY}'
EOF

# Execute Docker CMD
exec "$@"
