from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

org = "utem"
token = 'gaSO6nZV9Oe7Prkojlgg7GnJ3pj2zR7Plq56WZf-UIDfFFQFwUQ6GUZLyq-No9VzdEFXEb5MgYJbnO5idZbgrw=='
url="http://18.204.7.51:8086"

def influx_process(object):
    client = InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    bucket="test_py"
    # Write script
    write_api = client.write_api(write_options=SYNCHRONOUS)

    p = Point("Sensors")\
        .tag("device_id", object["tags"]["end_device_ids_device_id"])\
        .tag("rssi", object["tags"]["uplink_message_rx_metadata_0_rssi"])\
        .tag("snr", object["tags"]["uplink_message_rx_metadata_0_snr"])\
        .field("valor", object["fields"]["uplink_message_frm_payload"])
    write_api.write(bucket=bucket, org=org, record=p)

def query_influx():
    client = InfluxDBClient(
        url=url,
        token=token,
        org=org
    )
    query_api = client.query_api()
    query = 'from(bucket: "IoT")\
    |> range(start: -3h, stop: now())\
    |> filter(fn: (r) => r["_measurement"] == "Sensores")\
    |> last()'
    
    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            if record.get_field() == "temp":
                kpi = 1
            elif record.get_field() == "hum":
                kpi = 2
            results.append((record.values.get("id"),
                            record.get_value(),
                            record.values.get("estado"),
                            kpi,
                        ))
    return (results)