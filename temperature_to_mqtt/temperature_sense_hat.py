import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import socket
import time
import uuid

sensor = SenseHat()
broker_address="10.1.0.1" 

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

client_name = uuid.uuid4()
client = mqtt.Client(str(client_name)) #create new instance
client.connect(broker_address) #connect to broker
ip = get_ip_address() # get current IP so we can ID ourselves

while True:
	temperature_in_celsius = sensor.get_temperature()
	# print("Publishing message to topic","/house/temperature")
	client.publish("/house/temperature",'{"temperature": {"value": ' + str(temperature_in_celsius) + ', "units": "C"}, "from_ip": "' + str(ip) + '"}')
	time.sleep(5);
