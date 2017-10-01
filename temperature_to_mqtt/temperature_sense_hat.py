import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import socket
import time
import uuid

sensor = SenseHat()
broker_address="10.1.0.1" 

client = mqtt.Client() #create new instance
client.connect(broker_address) #connect to broker

while True:
	temperature_in_celsius = sensor.get_temperature()
	# print("Publishing message to topic","/house/temperature")
	# beware hardcoded identifier if you use more than one SenseHAT!
	client.publish("/house/temperature",'{"temperature": {"value": ' + str(temperature_in_celsius) + ', "units": "C"}, "sensor_id": "SenseHAT"}')
	time.sleep(5);
