import paho.mqtt.client as mqtt
from w1thermsensor import W1ThermSensor
import socket
import time

broker_address="10.1.0.1"

client = mqtt.Client() #create new instance
client.connect(broker_address) #connect to broker

while True:
    for sensor in W1ThermSensor.get_available_sensors():
        temperature_in_celsius = sensor.get_temperature()
        # print("Publishing message to topic","/house/temperature")
        client.publish("/house/temperature",'{"temperature": {"value": ' + str(temperature_in_celsius) + ', "units": "C"}, "sensor_id": ' + sensor.id + '}')

    time.sleep(5);

