from datetime import datetime
import random
from time import sleep

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "KjAGXKB3Mc15faOdLP_e_fHbiZkdUM8eB3ndEA6Ro5kSfB60xjF9PRevmni4R-PjidBtah8ALrGHoKaQLzcACw=="
org = "dc2df44416f0ee35"
bucket = "32706061e097327d"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)


write_api = client.write_api(write_options=SYNCHRONOUS)


## TEMPORARY TEST
while True:
    point = Point("mem")\
    .tag("name", "sensor_ph")\
    .field("value", random.randint(0,200))\
    .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket, org, point)
    sleep(3)