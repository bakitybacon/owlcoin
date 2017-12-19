#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import sys
import os
import time
import threading

blinkthread = None
blinking = False

gpio_num = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_num, GPIO.OUT)

def runleds(blink):

  global blinking

  if blink == 0:
    blinking = False
    GPIO.output(gpio_num, GPIO.LOW)

  elif blink == 1:
    blinking = True
    while blinking:
      GPIO.output(gpio_num, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(gpio_num, GPIO.LOW)
      time.sleep(0.1)
    if blink == 2:
      GPIO.output(gpio_num, GPIO.HIGH)
    elif blink == 0:
      GPIO.output(gpio_num, GPIO_LOW)

  elif blink == 2:
    blinking = False
    GPIO.output(gpio_num, GPIO.HIGH)

  else:
    blinking = False
    print "unknown signal!", blink

def handler(signum, frame):
#  print signum

  if signum == signal.SIGUSR1:
    runleds(0)
  elif signum == signal.SIGUSR2:
    blinkthread = threading.Thread(target = runleds, args = (1, ))
    blinkthread.start()
  elif signum == signal.SIGALRM:
    runleds(2)
  else:
    print "unknown signal!", signum

file = open('/home/pi/ledpid', 'w')
file.write(str(os.getpid()))
file.close()

signal.signal(signal.SIGUSR1, handler)
signal.signal(signal.SIGUSR2, handler)
signal.signal(signal.SIGALRM, handler)

while 1 < 2:
  time.sleep(5)
