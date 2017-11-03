import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)

print "Illuminating..."
GPIO.output(20, GPIO.HIGH)

time.sleep(2)

print "Extinguishing..."
GPIO.output(20, GPIO.LOW)

GPIO.cleanup()
