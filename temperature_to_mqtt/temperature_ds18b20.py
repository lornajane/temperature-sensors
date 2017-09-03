import paho.mqtt.client as mqtt
from w1thermsensor import W1ThermSensor
import socket
import time

sensor = W1ThermSensor()
broker_address="10.1.0.1" 

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
ip = get_ip_address() # get current IP so we can ID ourselves

while True:
	temperature_in_celsius = sensor.get_temperature()
	# print("Publishing message to topic","/house/temperature")
	client.publish("/house/temperature",'{"temperature": {"value": ' + str(temperature_in_celsius) + ', "units": "C"}, "from_ip": ' + str(ip) + '}')
	time.sleep(5);

