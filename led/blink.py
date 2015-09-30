#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

def blink(pin):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.5)

pin = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

for i in range(10):
	blink(pin)

GPIO.cleanup()
