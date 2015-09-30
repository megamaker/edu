#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	input_state = GPIO.input(pin)
	print input_state
	time.sleep(0.5)
