import paho.mqtt.client as mqtt
import time
from random import randrange, uniform

# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)

seats = [False, False] # seat1 and seat2
data = {
    "pulse_start1": 0,
    "pulse_end1": 0,
    "pulse_start2": 0,
    "pulse_end2": 0
}

# def ultrasonicSensorSetup(trigPin, echoPin):
#     GPIO.setup(trigPin, GPIO.OUT)
#     GPIO.setup(echoPin, GPIO.IN)

def runUltrasonicSensor(trigPin, echoPin, topic, seatNum):
    randNumber = round(uniform(0, 1))
    client.publish(topic, randNumber)
    print("Just published", randNumber, "to Topic", seatNum + 1)


mqttBroker = "broker.emqx.io" # alternative: mqtt.eclipseprojects.io

client = mqtt.Client("raspiteam14")
client.connect(mqttBroker)

topic1 = "ultrasonic1/nc3c6s2"
topic2 = "ultrasonic2/nc3c6s2"
topic3 = "ldr/nc3c6s2"

trigPin1 = 22
echoPin1 = 23

trigPin2 = 17
echoPin2 = 18

# ultrasonicSensorSetup(trigPin1, echoPin1)
# ultrasonicSensorSetup(trigPin2, echoPin2)

try:
    while True:
        runUltrasonicSensor(trigPin1, echoPin1, topic1, 0)
        time.sleep(0.5)

        runUltrasonicSensor(trigPin2, echoPin2, topic2, 1)
        time.sleep(0.5)

except KeyboardInterrupt:
    # GPIO.cleanup()
    print("DONE")
