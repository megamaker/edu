#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

pin23 = 23
pin18 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin18, GPIO.OUT)

def ledon():
	GPIO.output(pin18, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(pin18, GPIO.LOW)

while True:
	input_state = GPIO.input(pin23)
	if not input_state:
		ledon()
	time.sleep(0.1)
