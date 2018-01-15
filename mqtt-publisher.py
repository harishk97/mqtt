import paho.mqtt.client as mqtt
import time
broker_address="iot.eclipse.org"
#broker_address="192.168.1.102"


# This is the Publisher

client = mqtt.Client("p1")
client.connect(broker_address)
client.loop_start()
client.publish("test", "Hello world!")
client.disconnect()
client.loop_stop()
