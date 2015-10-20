#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 23
Motor1B = 24
Motor1E = 25

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

pwm = GPIO.PWM(Motor1E, 500)
pwm.start(0)

GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)

print 'Speed up'
for step in range(11):
	duty = step * 10
	print duty
	pwm.ChangeDutyCycle(duty)
	sleep(2)

print 'Speed down'
for step in range(11):
	duty = (10 - step) * 10
	print duty
	pwm.ChangeDutyCycle(duty)
	sleep(2)

print 'Stopping motor'
GPIO.output(Motor1E, GPIO.LOW)

GPIO.cleanup()
