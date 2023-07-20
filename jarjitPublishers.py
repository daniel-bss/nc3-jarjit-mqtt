import paho.mqtt.client as mqtt
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

seats = [False, False] # seat1 and seat2
data = {
    "pulse_start1": 0,
    "pulse_end1": 0,
    "pulse_start2": 0,
    "pulse_end2": 0
}

def ultrasonicSensorSetup(trigPin, echoPin):
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

def runUltrasonicSensor(trigPin, echoPin, topic, seatNum):
    GPIO.output(trigPin, False)
    time.sleep(0.08)
    GPIO.output(trigPin, True)
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    
    while GPIO.input(echoPin) == 0:
        data[f"pulse_start{seatNum + 1}"] = time.time()
        
    while GPIO.input(echoPin) == 1:
        data[f"pulse_end{seatNum + 1}"] = time.time()
        
    pulse_duration = data[f"pulse_end{seatNum + 1}"] - data[f"pulse_start{seatNum + 1}"]
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print(f"distance {seatNum + 1}", distance)

    if distance < 10:
        seats[seatNum] = True
    else:
        seats[seatNum] = False

    client.publish(topic, int(seats[seatNum]))
    # print("Just published", int(seats[seatNum]), "to Topic", seatNum + 1)


mqttBroker = "broker.emqx.io" # alt: mqtt.eclipseprojects.io

client = mqtt.Client("raspiteam14")
client.connect(mqttBroker)

topic1 = "ultrasonic1/ular melingkar di atas pagar"
topic2 = "ultrasonic2/ular melingkar di atas pagar"
topic3 = "ldr/ular melingkar di atas pagar"

trigPin1 = 22
echoPin1 = 23

trigPin2 = 17
echoPin2 = 18

ultrasonicSensorSetup(trigPin1, echoPin1)
ultrasonicSensorSetup(trigPin2, echoPin2)


try:
    while True:
        runUltrasonicSensor(trigPin1, echoPin1, topic1, 0)
        time.sleep(0.05)

        runUltrasonicSensor(trigPin2, echoPin2, topic2, 1)
        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()
