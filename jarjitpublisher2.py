import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "broker.emqx.io"

client = mqtt.Client("ldr")
client.connect(mqttBroker)

topic2 = "ldr/ular melingkar di atas pagar"

while True:
    randNumber = round(uniform(0, 1))
    client.publish(topic2, randNumber)
    print("Just published " + str(randNumber) + " to Topic 2")
    time.sleep(0.5)
