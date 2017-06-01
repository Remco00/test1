import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 50)

p.start(11)

try:
    while True:
        #unlocked
        p.ChangeDutyCycle(6)
        sleep(1)

        #locked
        p.ChangeDutyCycle(11)
        sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()