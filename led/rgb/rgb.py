#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

def gpio_high():
	GPIO.output(bluePin, GPIO.HIGH)
	GPIO.output(greenPin, GPIO.HIGH)
	GPIO.output(redPin, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)

anodePin = 18
bluePin = 23
greenPin = 24
redPin = 25

GPIO.setup(anodePin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT)
GPIO.output(anodePin, GPIO.HIGH)

try:
	while True:
		gpio_high()
		GPIO.output(redPin, GPIO.LOW)
		time.sleep(0.5)
		gpio_high()
		GPIO.output(greenPin, GPIO.LOW)
		time.sleep(0.5)
		gpio_high()
		GPIO.output(bluePin, GPIO.LOW)
		time.sleep(0.5)
except KeyboardInterrupt:
	gpio_high()
	GPIO.cleanup()
