import RPi.GPIO as GPIO
import time

inPin1: int = 40
outPin1: int = 11

ldr = 7
dt = 0.1

GPIO.setmode(GPIO.BOARD)
# GPIO.setup(inPin1, GPIO.IN)
# GPIO.setup(outPin1, GPIO.OUT)



def getLdr(ldr):
    count = 0
    
    # GPIO.setup(ldr, GPIO.OUT)
    # GPIO.output(ldr, False)

    # time.sleep(dt)

    GPIO.setup(ldr, GPIO.IN)


    # while GPIO.input(ldr) == 0:
    #     print(GPIO.input(ldr))
    #     count += 1

    # return count
    print(GPIO.input(ldr))
    return 1
try:
    while True:
        value = getLdr(ldr)
        # print(value)
except KeyboardInterrupt:
    GPIO.cleanup()
    

