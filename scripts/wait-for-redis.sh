#!/usr/bin/env bash

HOST=$1
shift
PORT=$1
shift
CLI=("$@")

echo "Start waiting for Redis to fully start. Host '$HOST:$PORT'..."
echo "Try ping Redis... "
PONG=`redis-cli -h $HOST -p $PORT ping | grep PONG`
while [ -z "$PONG" ]; do
    sleep 3
    echo "Retry Redis ping..."
    PONG=`redis-cli -h $HOST -p $PORT ping | grep PONG`
done
echo "Redis at host '$HOST:$PORT' fully started."

exec "${CLI[@]}"
