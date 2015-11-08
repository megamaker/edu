#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledPin = 18
GPIO.setup(ledPin, GPIO.OUT)

try:
	while True:
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(ledPin, GPIO.LOW)
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()
