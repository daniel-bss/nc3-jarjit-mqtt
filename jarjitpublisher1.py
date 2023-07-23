import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "broker.emqx.io"

client = mqtt.Client("ultrasonic")
client.connect(mqttBroker)

topic1 = "ultrasonic/nc3c6s2"
topic2 = "ldr/nc3c6s2"

def publisher1():
    randNumber1 = round(uniform(0, 1))
    client.publish(topic1, randNumber1)
    print("Just published " + str(randNumber1) + " to Topic 1")

def publisher2():
    randNumber2 = round(uniform(0, 1))
    client.publish(topic2, randNumber2)
    print("Just published " + str(randNumber2) + " to Topic 2")

while True:
    publisher1()
    time.sleep(0.25)
    
    publisher2()
    time.sleep(0.25)
    
