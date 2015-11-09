#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

def gpio_low():
	GPIO.output(redPin,    GPIO.LOW)
	GPIO.output(yellowPin, GPIO.LOW)
	GPIO.output(greenPin,  GPIO.LOW)

swPin = 18
redPin = 23
yellowPin = 24
greenPin = 25

GPIO.setmode(GPIO.BCM)

GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(yellowPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

gpio_low()

try:
	led_status = 0
	release_status = 0
	while True:
		sw_status = GPIO.input(swPin)

		if sw_status == False:
			release_status = 1
			print 'led_status', led_status
			if led_status == 0:
				gpio_low()
				GPIO.output(redPin, GPIO.HIGH)
			elif led_status == 1:
				gpio_low()
				GPIO.output(yellowPin, GPIO.HIGH)
			elif led_status == 2:
				gpio_low()
				GPIO.output(greenPin, GPIO.HIGH)

		elif sw_status == True:
			if release_status:
				release_status = 0
				led_status += 1
				if led_status > 2:
					led_status = 0
except KeyboardInterrupt:
	gpio_low()
	GPIO.cleanup()
