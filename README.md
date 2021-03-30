This project helps to run the development environment of [le.taxi](https://le.taxi/) locally. It heavily relies on Docker and docker-compose.

# How does it work?

## Services

This is the list of services run by APITaxi_devel.

* **api**: our main API, [APITaxi](github.com/openmaraude/APITaxi) used by operators and search providers to register and request taxis.
* **console**: frontend used by operators and search providers to see dashboards, manage credentials and access documentation.
* **worker**: asynchronous celery tasks of **api**.
* **worker-beat**: [celery-beat](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html) process, to run periodic tasks to clean database or store statistics.
* **geotaxi**: UDP server which receives real-time locations from operators and store them in **redis**.
* **minimal-operateur-server**: our example project of an [operator API](https://github.com/openmaraude/minimal_operateur_server), which receives hail requests from APITaxi.
* **minimal-operateur-server-worker**: [python-rq](https://python-rq.org/) project to run asynchronous tasks of **minimal_operateur_server**.
* **map**: javascript widget to display available taxis on a map.
* **geofaker**: [custom project](https://github.com/openmaraude/geofaker) to send fake data to **geotaxi**.
* **db**: PostgreSQL backend of **api** and **worker**.
* **redis**: redis backend of **api**, **worker**, and **geotaxi**. Contains taxis locations in real-time. Also used as [celery](https://docs.celeryproject.org) broker.
* **swagger**: web interface to expose the API reference documentation. Documentation is retrieved from the **api** endpoint `/swagger.json`.
* **flower**: [celery-flower](https://flower.readthedocs.io) web interface to monitor celery tasks.
* **fluentd**: [fluentd](https://www.fluentd.org/) is an opensource data collector, which receives logs from **geoataxi**.
* **influxdb**: [influxdb](https://www.influxdata.com/) is an opensource time series database which stores statistics generated by **worker**, displayed in **grafana** and read by **api**.
* **grafana**: [grafana](https://grafana.com/) is an opensource visualization dashboard which displays data stored in **influxdb**.


## File structure

* [docker-compose.yml](docker-compose.yml) declares all the infrastructure components: APIs, databases, workers. "Homemade" projects like APIs and workers use images built by the [Makefile](Makefile). Other containers use images published on the docker hub (postgres, redis, ...).
* [Makefile](Makefile) contains commands often executed when you work locally. Run `make build` to build the docker images required by docker-compose, `make up` to start all containers, and `make logs` to view logs.
* [containers/](containers/) gathers Dockerfiles, Docker entrypoints, and configuration files to create the development version of homemade images.
* [projects/](projects/) contains git submodules to other projects.
* [scripts/](scripts/) is a set of scripts that are only useful when developing locally.


## Autoreload

When the code of our projects change from the host, servers inside containers reload automatically. To understand how, let's see how [APITaxi](https://github.com/openmaraude/APITaxi) is setup:

- [docker-compose.yml](docker-compose.yml) mounts the submodule `./projects/APITaxi` to `/git/APITaxi`, so any modification from the host is visible inside the container.
- when the containers `api` starts, the entrypoint ([containers/api/entrypoint.sh](containers/api/entrypoint.sh)) installs `/git/APITaxi` as an [editable install](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).
    * *Python editable install: when you install a project with `pip install .`, source code is copied inside the virtualenv and modifications require to re-run the installation to see changes inside the virtualenv. With `pip install -e .`, only a link is installed so restarting the application is enough to see changes.*
- the API is served by `flask run`. Since `FLASK_DEBUG` is set in the [Docker image](containers/api/Dockerfile), changes are monitored and flask reloads automatically.


# Installation

### Pull submodules

```
$> make update-submodules
```

### Run containers

```
$> make up
```

Behind the scene, `make up` calls `make build` to create containers and `docker-compose up -d` to launch containers.

Wait until the installation finishes. To view logs, run `make logs`.

**Note**: at this point, the containers `minimal-operateur-server` and `minimal-operateur-server-worker` can't work. Their entrypoints require the `db` container to be setup and have data.

### Create databases

```
$> docker-compose exec db psql -U postgres
# CREATE DATABASE taxis;
# \c taxis
# CREATE EXTENSION postgis;
```

Restore databases (postgres, redis, influx) from production to have data.


# Operations

When your stack is setup, chances are you will need the commands below.

## Play with Docker

Containers can be all started automatically with `make up`. You might prefer to run it manually to override the docker `CMD`. For example, for the `api` container:

```
$> docker-compose run --rm --service-ports --name api api bas
```

By default, `docker-compose run` starts dependencies. Add `--no-deps` to override this behavior.

## Databases migrations

### Apply migrations

```
$> docker-compose exec api bash
(api)> cd APITaxi_models2/
(api)> alembic upgrade head
```

### Generate a new migration file

Databases migrations are managed by [alembic](https://alembic.sqlalchemy.org). If your models change, you need to create a new migration file.

```
$> docker-compose exec api bash
(api)> cd APITaxi_models2/
(api)> alembic revision --autogenerate -m 'update'
```

Make sure to review the generated file and to remove anything that might have been created automatically by alembic.
