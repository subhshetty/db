import json
from influxdb import InfluxDBClient
from datetime import datetime
current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'test3')

client.create_database('test3')

def read_data():
    with open('a1.txt') as f:
        return [x.split(',') for x in f.readlines()[1:]]

a = read_data()

for metric in a:
    influx_metric = [{
        'measurement': 'your_measurement1',
	'tags': {
            'host': metric[0],
        },
	'time': current_time,
        'fields': {
             'value_a': metric[1],
             'value_b': metric[2]
        }
    }]
    client.write_points(influx_metric)
