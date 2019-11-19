#!/usr/bin/env python

"""This script assumes the containers "db" and "geofaker" are up, and container
"db" contains a seeded database.

By default, "geofaker" uses fake data to feed geotaxi. This script reads the
taxi id stored in "db", and generates valid configuration file, so geotaxi
can update positions of real taxis in redis.
"""

import argparse
import csv
import logging
import subprocess
import tempfile


logger = logging.getLogger(__name__)


def generate_config(limit):
    with tempfile.NamedTemporaryFile(mode='w') as tmpfile:
        writer = csv.writer(tmpfile)

        # Get taxi ids from table "taxi"
        logger.info('Get %s taxis from table taxi in container "db"', limit)
        try:
            output = subprocess.check_output([
                'docker-compose', 'exec', 'db',
                'psql', '-U', 'postgres', 'taxis',
                '-q', '-t', '-P', 'pager=off', '-c',
                """select taxi.id, "user".apikey, "user".email from taxi JOIN "ADS" ON "ADS".id = taxi.ads_id JOIN "user" ON "user".id = taxi.added_by JOIN "ZUPC" ON "ZUPC".id = "ADS".zupc_id WHERE "ZUPC".insee = '75101' LIMIT %s;""" % limit
            ])
        except subprocess.CalledProcessError as e:
            print(e.output)
            raise e
        for row in output.splitlines():
            if not row:
                continue
            taxi_id, api_key, operator = [s.strip() for s in  row.decode('utf-8').split('|')]

            writer.writerow(
                [
                    operator,  # operator
                    '2',         # version
                    taxi_id,     # taxi id
                    '0',         # ?
                    '0',         # ?
                    'free',      # status
                    'mobile',    # device
                    'hash',      # hash type
                    api_key    # api key
                ]
            )

        tmpfile.flush()

        logger.info("Get docker id of geofaker")
        geofakerid = subprocess.check_output(["docker-compose", "ps", "-q", "geofaker"]).decode('utf-8').strip()

        logger.info('Store CSV file into container "geofaker"')
        subprocess.call([
            'docker', 'cp', tmpfile.name, '%s:/taxis_file.csv' % geofakerid
        ])
        logger.info('Fix file chmod into container "geofaker"')
        subprocess.call([
            'docker', 'exec', geofakerid,
            'sudo', 'chown', 'geofaker:geofaker', '/taxis_file.csv'
        ])
        subprocess.call([
            'docker-compose', 'restart', 'geofaker'
        ])

def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--limit', type=int, default=1,
                        help='Limit of taxis to generate configuration for')
    args = parser.parse_args()

    generate_config(args.limit)


if __name__ == '__main__':
    main()
