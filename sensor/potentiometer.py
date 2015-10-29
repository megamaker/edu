#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

powerPin = 23
signalPin = 18
ledPin = 24

GPIO.setup(ledPin, GPIO.OUT)
pwm = GPIO.PWM(ledPin, 500)
pwm.start(0)

def discharge():
	GPIO.setup(powerPin, GPIO.IN)
	GPIO.setup(signalPin, GPIO.OUT)
	GPIO.output(signalPin, GPIO.LOW)
	time.sleep(0.05)

def charge_time():
	GPIO.setup(signalPin, GPIO.IN)
	GPIO.setup(powerPin, GPIO.OUT)
	GPIO.output(powerPin, GPIO.HIGH)
	count = 0
	while not GPIO.input(signalPin):
		count = count + 1
	return count

def analog_read():
	discharge()
	return charge_time()

def normalize(analogValue):
	analogMin = 30
	analogMax = 300
	shiftMin = min - min
	shiftMax = max - min
	normalRange = float(shiftMax - shiftMin)

	if analogValue < analogMin:
		analogValue = analogMin
	if analogValue > analogMax:
		analogValue = analogMax

	normalizeValue = (analogValue - analogMin) / normalRange
	return int(normailizeValue * 100)

while True:
	analogValue = analog_read()
	normalizeValue = normalize(analogValue)
	print analogValue, normalizeValue
	pwm.ChangeDutyCycle(normalizeValue)
	time.sleep(0.05)
