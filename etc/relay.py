#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

pin = 18 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

try:
	while True:
		GPIO.output(pin, GPIO.HIGH)
except KeyboardInterrupt:
	GPIO.output(pin, GPIO.LOW)
	GPIO.cleanup()
