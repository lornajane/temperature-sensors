import paho.mqtt.client as mqtt
from w1thermsensor import W1ThermSensor
import time

sensor = W1ThermSensor()
broker_address="10.1.0.1" 
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker

while True:
	temperature_in_celsius = sensor.get_temperature()
	# print("Publishing message to topic","/house/temperature")
	client.publish("/house/temperature",'{"temperature": {"value": ' + str(temperature_in_celsius) + ', "units": "C"}}')
	time.sleep(5);

