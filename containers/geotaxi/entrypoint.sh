#!/bin/sh

kill_running_server() {
    pkill --signal SIGKILL geoloc-server
}

run_geoloc_server() {
    kill_running_server
    wait-for-it redis:6379 -- ./geoloc-server -p 8080 --redisurl redis &
}

cd /git/geotaxi

# Kill server on ctrl+c
trap 'kill_running_server' TERM INT

# Run server
make
run_geoloc_server

# On change, recompile and run server
while inotifywait -o /dev/null -r --exclude '.*git.*' /git/geotaxi 2>/dev/null
do
    echo "Changes detected, recompile and restart server" >&2
    make
    run_geoloc_server
done
