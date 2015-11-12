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
	#print 'period', period, 'delay', delay, 'cycles', cycles
	for i in range(cycles):
		GPIO.output(buzzerPin, True)
		time.sleep(delay)
		GPIO.output(buzzerPin, False)
		time.sleep(delay)

scale = {'C':261, 'D':294, 'E':329, 'F':349, 'G':392, 'A':440}
song = ['G', 'G', 'A', 'A', 'G', 'G', 'E', 
	    'G', 'G', 'E', 'E', 'D', 
		'G', 'G', 'A', 'A', 'G', 'G', 'E', 
		'G', 'E', 'D', 'E', 'C']

count = 0
for s in song:
	duration = 0.5
	if count == 6 or count == 18:
		duration = 1
	if count == 11 or count == 23:
		duration = 1.5
	print s
	buzz(scale[s], duration)
	count += 1

GPIO.cleanup()
