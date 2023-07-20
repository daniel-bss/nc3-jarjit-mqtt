import RPi.GPIO as GPIO
import time

inPin1: int = 40
outPin1: int = 11

irPin = 7
dt = 0.1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(irPin, GPIO.IN)

try:
    while True:
        print(GPIO.input(irPin))
        # if GPIO.input(irPin) == 0:
        #     print("detecting")
        #     time.sleep(dt)
        # else:
        #     print("not detecting")
        #     time.sleep(dt)

except KeyboardInterrupt:
    GPIO.cleanup()
    

