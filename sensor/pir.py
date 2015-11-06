#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pirPin = 18
ledPin = 21
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

try:
	time.sleep(1)
	print 'ready'

	while True:
		if GPIO.input(pirPin):
			print 'motion detected'
			GPIO.output(ledPin, GPIO.HIGH)
			time.sleep(3)
			GPIO.output(ledPin, GPIO.LOW)

except KeyboardInterrupt:
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()
