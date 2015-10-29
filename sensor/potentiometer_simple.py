#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledPin = 23

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.HIGH)

while True:
	pass
