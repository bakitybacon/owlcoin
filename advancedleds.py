#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

if not len(sys.argv) >= 2:
	print "Usage: advancedleds time blink gpio-number"
	sys.exit(1)

maxtime = int(sys.argv[1])
blink = False
if len(sys.argv) >= 3:
	blink = sys.argv[2] == "blink"

gpio_num = 20

if len(sys.argv) >= 4:
	gpio_num = int(sys.argv[3])

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(gpio_num, GPIO.OUT)

	if blink:
		currtime = time.time()
#		print "Blinking..."
		for dummy in range(5 * maxtime):
			GPIO.output(gpio_num, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(gpio_num, GPIO.LOW)
			time.sleep(0.1)
#		print "Done!"
#		print "Elapsed Time:", (time.time() - currtime)
	
	else:
#		print "Illuminating..."
		GPIO.output(gpio_num, GPIO.HIGH)
	
		time.sleep(maxtime)

#		print "Extinguishing..."
		GPIO.output(gpio_num, GPIO.LOW)
finally:
#	print "cleaning up..."
	GPIO.output(gpio_num, GPIO.LOW)
	GPIO.cleanup()
