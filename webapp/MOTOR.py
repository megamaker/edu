#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import sys

direction = sys.argv[1] # F or B or S
speed = int(sys.argv[1]) # 1 or 2 or 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Motor1A = 23
Motor1B = 24
Motor1E = 25
Motor1AStatus = None
Motor1BStatus = None
Motor1EStatus = None

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

if direction == 'S':
	Motor1EStatus = GPIO.HIGH
	if direction == 'F':
		Motor1AStatus = GPIO.HIGH
		Motor1BStatus = GPIO.LOW
	elif direction == 'B':
		Motor1AStatus = GPIO.LOW
		Motor1BStatus = GPIO.HIGH
else:
	Motor1EStatus = GPIO.LOW
GPIO.output(Motor1A, Motor1AStatus)
GPIO.output(Motor1B, Motor1BStatus)
GPIO.output(Motor1E, Motor1EStatus)

pwm = GPIO.PWM(Motor1E, 500)
pwm.start(0)
if speed == 1:
	pwm.ChangeDutyCycle(20)
elif spped == 2:
	pwm.ChangeDutyCycle(60)
elif spped == 3:
	pwm.ChangeDutyCycle(100)
