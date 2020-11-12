#!/usr/bin/env python3

import argparse
import hashlib
import json
import socket
import time


def get_location_request(lon, lat, taxi_id, operator, apikey):
    """Payload to send to geotaxi to update taxi location."""
    payload = {
        'timestamp': int(time.time()),
        'operator': operator,
        'taxi': taxi_id,
        'lat': lat,
        'lon': lon,
        'device': 'phone',
        'status': 'free',
        'version':'2',
    }
    h = ''.join(
        str(payload[k]) for k in ['timestamp', 'operator', 'taxi', 'lat', 'lon', 'device', 'status', 'version']
    )
    h += apikey
    payload['hash'] = hashlib.sha1(h.encode('utf-8')).hexdigest()
    return json.dumps(payload).encode('ascii')


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '--api-key', default='00000000-0000-0000-0000-000000000000',
        help='API key to compute hash. Only required if Geotaxi runs with --auth-enabled'
    )
    parser.add_argument('--host', default='localhost', help='Geotaxi host')
    parser.add_argument('--port', type=int, default=8080, help='Geotaxi port')
    parser.add_argument('--lon', type=float, default=2.35, help='Taxi longitude')
    parser.add_argument('--lat', type=float, default=48.86, help='Taxi latitude')
    parser.add_argument('--operator', required=True, help='Taxi operator name')
    parser.add_argument('--taxi', required=True, help='Taxi id')

    args = parser.parse_args()

    data = get_location_request(args.lon, args.lat, args.taxi, args.operator, args.api_key)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, (args.host, args.port))


if __name__ == '__main__':
    main()
