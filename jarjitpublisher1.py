import paho.mqtt.client as mqtt
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

isSeat1Occupied = False

TRIG=21
ECHO=20

def ultrasonicSensorSetup(trigPin, echoPin):
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

def runUltrasonicSensor(trigPin, echoPin, topic):
    GPIO.output(trigPin, False)
    time.sleep(0.1)
    GPIO.output(trigPin, True)
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    
    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()
        
    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    if distance < 4:
        isSeat1Occupied = True
    else:
        isSeat1Occupied = False

    client.publish(topic, int(isSeat1Occupied))
    print("Just published", int(isSeat1Occupied), "to Topic 1")


mqttBroker = "broker.emqx.io" # alt: mqtt.eclipseprojects.io

client = mqtt.Client("raspiteam14")
client.connect(mqttBroker)

topic1 = "ultrasonic/ular melingkar di atas pagar"
# topic2 = "ldr/ular melingkar di atas pagar"

# def publisher1():
#     randNumber1 = round(uniform(0, 1))
#     client.publish(topic1, randNumber1)
#     print("Just published " + str(randNumber1) + " to Topic 1")

# def publisher2():
#     randNumber2 = round(uniform(0, 1))
#     client.publish(topic2, randNumber2)
#     print("Just published " + str(randNumber2) + " to Topic 2")

ultrasonicSensorSetup(TRIG, ECHO)

try:
    while True:
        runUltrasonicSensor(TRIG, ECHO, topic1)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    
