#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

swPin = 18
ledPin = 23

GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)

try:
	while True:
		input_state = GPIO.input(swPin)
		if input_state == True:
			GPIO.output(ledPin, GPIO.LOW)
		else:
			GPIO.output(ledPin, GPIO.HIGH)
except KeyboardInterrupt:
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()
