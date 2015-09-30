#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO

pinSW = 12
pinLED = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinSW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinLED, GPIO.OUT)

while True:
	input_state = GPIO.input(pinSW)
	if input_state == True:
		GPIO.output(pinLED, GPIO.LOW)
	else:
		GPIO.output(pinLED, GPIO.HIGH)
