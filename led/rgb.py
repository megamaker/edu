#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

anode = 18
blue = 23
green = 24
red = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(anode, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

GPIO.output(anode, GPIO.HIGH)

def emit(r, g, b):
	GPIO.output(blue, GPIO.HIGH)
	GPIO.output(green, GPIO.HIGH)
	GPIO.output(red, GPIO.HIGH)
	if r:
		GPIO.output(red, GPIO.LOW)
	if g:
		GPIO.output(green, GPIO.LOW)
	if b:
		GPIO.output(blue, GPIO.LOW)

while True:
	emit(1, 0, 0)
	time.sleep(0.5)
	emit(0, 1, 0)
	time.sleep(0.5)
	emit(0, 0, 1)
	time.sleep(0.5)

GPIO.cleanup()
