import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup('P8_10', GPIO.OUT)

while True:
    GPIO.output('P8_10', GPIO.HIGH)
    time.sleep(1)
    GPIO.output('P8_10', GPIO.LOW)
    time.sleep(1)