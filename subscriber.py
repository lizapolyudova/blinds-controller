import paho.mqtt.client as mqtt
import time

broker_address = "172.16.16.107"
port = 1883
Connected = False #global variable for the state of the connection

client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message

client.connect(broker_address, port=port)  #connect to broker
client.loop_start()                        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("python/test")