#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

powerPin = 18
signalPin = 23
ledPin = 24

GPIO.setup(ledPin, GPIO.OUT)
pwm = GPIO.PWM(ledPin, 500)
pwm.start(0)

def discharge():
	GPIO.setup(powerPin, GPIO.IN)
	GPIO.setup(signalPin, GPIO.OUT)
	GPIO.output(signalPin, False)
	time.sleep(0.05)

def charge_time():
	GPIO.setup(signalPin, GPIO.IN)
	GPIO.setup(powerPin, GPIO.OUT)
	count = 0
	GPIO.output(powerPin, True)
	while not GPIO.input(signalPin):
		count = count + 1
	return count

def analog_read():
	discharge()
	return charge_time()

while True:
	analogValue = analog_read()
	print analogValue,
	if analogValue < 30:
		analogValue = 30
	if analogValue > 300:
		analogValue = 300
	print analogValue / 3
	pwm.ChangeDutyCycle(analogValue / 3)
	time.sleep(0.05)
