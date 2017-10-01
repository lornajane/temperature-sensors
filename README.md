# Temperature Sensors Code

A repo to keep the code for the various not-quite-the-same devices we use to measure temperature in the house.  These are almost entirely Raspberry Pi 3s with DS18B20 sensors, but there are also some Pi 2s, a Pi zero and a Pi3 wearing a SenseHat.  The temperature readings are published to MQTT and you'll also find the script that writes to PostgreSQL.

## To install a sensor

Clone the repo, run `pip3 install -r requirements.txt` in the `temperature_to_mqtt` directory.  Then set up a script to automatically run the appropriate script for your pi when it boots (something like this https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)

My script is `/lib/systemd/system/temperature.service` and it looks like this:

```
[Unit]
Description=Temperature Monitoring Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/pi/code/temperature-sensors/temperature_to_mqtt/temperature_sense_hat.py

[Install]
WantedBy=multi-user.target

```

## To install the server part

The server part will listen to MQTT and the messages from all the sensors, and write the values to a postgresql database.

The database needs a table called `temperature_reading` which looks like this:

```
house_metrics=> \d temperature_reading
                                                     Table "public.temperature_reading"
         Column         |            Type             |                                      Modifiers                                       
------------------------+-----------------------------+--------------------------------------------------------------------------------------
 temperature_reading_id | integer                     | not null default nextval('temperature_reading_temperature_reading_id_seq'::regclass)
 sensor_id              | character varying(100)      | not null
 created_at             | timestamp without time zone | 
 value                  | real                        | 
 units                  | character varying(10)       | 
Indexes:
    "temperature_reading_id" PRIMARY KEY, btree (temperature_reading_id)

```

The code is in `/mqtt_to_postgres/postgres.py` and this script needs the environment variable `PGPASSWORD` when it is run.  Run `pip3 install -r requirements.txt` in the directory to get the dependencies, then run the script like this:

```
PGPASSWORD=secret python3 postgres.py
```

As for the sensor, this code wants to live under systemd or similar since if any readings are missed, they can't be recovered.


