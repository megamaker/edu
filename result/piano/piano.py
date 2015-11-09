#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

def buzz(pitch, duration):
	period = 1.0 / pitch
	delay = period / 2
	cycles = int(duration * pitch)
	print 'period', period, 'delay', delay, 'cycles', cycles
	for i in range(cycles):
		GPIO.output(buzzerPin, True)
		time.sleep(delay)
		GPIO.output(buzzerPin, False)
		time.sleep(delay)

buzzerPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

cPin = 26
dPin = 19
ePin = 13
fPin = 21
gPin = 20
aPin = 16
GPIO.setup(cPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(fPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(aPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

duration = 0.2
try:
	while True:
		# 261 294 329 349 392 440 493 523
		if not GPIO.input(cPin): buzz(261, duration)
		if not GPIO.input(dPin): buzz(294, duration)
		if not GPIO.input(ePin): buzz(329, duration)
		if not GPIO.input(fPin): buzz(349, duration)
		if not GPIO.input(gPin): buzz(392, duration)
		if not GPIO.input(aPin): buzz(440, duration)
except KeyboardInterrupt:
	GPIO.cleanup()
