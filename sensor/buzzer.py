#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

buzzerPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

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

try:
	while True:
		pitch_s = raw_input("Enter Pitch (200 to 2000): ")
		pitch = float(pitch_s)
		duration_s = raw_input("Ener Duration (second): ")
		duration = float(duration_s)
		buzz(pitch, duration)
except KeyboardInterrupt:
	GPIO.cleanup()
