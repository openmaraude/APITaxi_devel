
Development environment to run APITaxi.


Installation
============

This project is still new and some steps might be non-working or require some manual actions.

To setup the API locally, use the following steps:

### Run containers

```
make up
```

Behind the scene, `make up` calls `make build` to create containers and `docker-compose up -d` to launch containers.

### Create database

```
$> docker-compose exec db psql -U postgres
# CREATE DATABASE taxis;
# \c taxis
# CREATE EXTENSION postgis;
```

### Apply schema migration

```
$> docker-compose exec api bash
# python manage.py db upgrade
```

### Create administrator user

```
$> docker-compose exec api bash
# python manage.py create_admin admin@localhost
```

### Retrieve your API key

```
$> docker-compose exec db psql -U postgres taxis -c 'SELECT email, apikey FROM "user"'
```

### Make your first HTTP request

```
$> curl -H 'X-Version: 2' \
        -H 'X-Api-key: <YOUR API KEY>' \
        -H 'Accept: application/json' \
        localhost:5000/
```
