#!/bin/sh

set -e

# If settings already exists, execute CMD
test -f /settings/settings.py && exec "$@"

# Otherwise, install PostgreSQL and get the apikey from user "neotaxi".
apt-get update -q
apt-get install -qqqy postgresql-client

API_KEY=$(psql -h db -U postgres taxis -t -c "SELECT apikey FROM \"user\" WHERE email = 'neotaxi'" | xargs)

if [ "$API_KEY" = "" ];
then
    echo "Unable to get apikey for user neotaxi" >&2
    exit 1
fi

cat<<EOF > /settings/settings.py
RQ_REDIS_URL = 'redis://redis:6379/0'
API_TAXI_URL = 'http://api:5000'
API_TAXI_KEY = '${API_KEY}'
EOF

exec "$@"
