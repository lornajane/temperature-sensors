import paho.mqtt.client as mqtt
import json
import psycopg2

def on_connect(client, userdata, flags, rc):
    client.subscribe("/house/temperature")

def on_message(client, userdata, msg):
    data = json.loads((msg.payload).decode("utf8"))
    sensor_pieces = data['from_ip'].split('.')

    cur = conn.cursor()
    cur.execute("INSERT INTO temperature_reading (sensor_id, created_at, value, units) VALUES (%(sensor_id)s, NOW(), %(value)s, 'C');", {'sensor_id': sensor_pieces[3], 'value': data['temperature']['value']})
    conn.commit()

# set up MQTT client
broker_address="10.1.0.1"
client = mqtt.Client("S1")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)

# set up database connection
conn = psycopg2.connect(dbname="house_metrics", user="pi", host="127.0.0.1")

client.loop_forever()
