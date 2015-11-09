#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

SW         = 12
LED_RED    = 22
LED_YELLOW = 24
LED_GREEN  = 26

GPIO.setmode(GPIO.BOARD)

GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(LED_RED,    GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN,  GPIO.OUT)

GPIO.output(LED_RED,    GPIO.LOW)
GPIO.output(LED_YELLOW, GPIO.LOW)
GPIO.output(LED_GREEN,  GPIO.LOW)

led_status = 0
release_status = 0
while True:
	sw_status = GPIO.input(SW)

	if sw_status == False:
		release_status = 1
		print 'led_status', led_status
		if led_status == 0:
			GPIO.output(LED_RED,    GPIO.HIGH)
			GPIO.output(LED_YELLOW, GPIO.LOW)
			GPIO.output(LED_GREEN,  GPIO.LOW)
		elif led_status == 1:
			GPIO.output(LED_RED,    GPIO.LOW)
			GPIO.output(LED_YELLOW, GPIO.HIGH)
			GPIO.output(LED_GREEN,  GPIO.LOW)
		elif led_status == 2:
			GPIO.output(LED_RED,    GPIO.LOW)
			GPIO.output(LED_YELLOW, GPIO.LOW)
			GPIO.output(LED_GREEN,  GPIO.HIGH)

	elif sw_status == True:
		if release_status:
			release_status = 0
			led_status += 1
			if led_status > 2:
				led_status = 0
