# Temperature Sensors Code

A repo to keep the code for the various not-quite-the-same devices we use to measure temperature in the house.  These are almost entirely Raspberry Pi 3s with DS18B20 sensors, but there are also some Pi 2s, a Pi zero and a Pi3 wearing a SenseHat.  The temperature readings are published to MQTT and you'll also find the script that writes to PostgreSQL.

## To install a sensor

Clone the repo, run `pip3 install -r requirements.txt` in the `temperature_to_mqtt` directory.  Then set up a script to automatically run the appropriate script for your pi when it boots (something like this https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)


