from datetime import datetime
import time

import paho.mqtt.client as mqtt
from gpiozero import CPUTemperature
from signal import pause


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


broker_address = "homeassistant"
port = 1883
mqtt_topic = "virtual-device"
Connected = False  # global variable for the state of the connection


def on_publish(client, userdata, result):  # create function for callback
    print(f"""{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} published data\n""")
    pass

print("publishing")
client = mqtt.Client("test-device")
client.on_publish = on_publish
print("connecting")
client.connect(broker_address, port)
print("connected, publishing")


while True:
    client.publish(mqtt_topic, CPUTemperature(min_temp=0, max_temp=100).value * 100, retain=True)
    time.sleep(10)
