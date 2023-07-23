import paho.mqtt.client as mqtt
from random import randrange, uniform

import time

mqttBroker = "broker.emqx.io" # alternative: mqtt.eclipseprojects.io

client = mqtt.Client("raspiteam14-carsweight")
client.connect(mqttBroker)

topic = "carsweight/nc3c6s2"

try:
    while True:
        randomCarWeight = f"{round(uniform(0, 101))}-{round(uniform(0, 101))}-{round(uniform(0, 101))}-{round(uniform(0, 101))}-{round(uniform(0, 101))}-{round(uniform(0, 101))}"
        client.publish(topic, randomCarWeight)
        print("Just published", randomCarWeight, "to Topic Cars Weight")
        time.sleep(2)
except KeyboardInterrupt:
    print("DONE")
