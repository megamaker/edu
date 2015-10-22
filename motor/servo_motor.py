#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor = 18

GPIO.setup(motor, GPIO.OUT)
pwm = GPIO.PWM(motor, 100)
pwm.start(0)

#GPIO.output(motor, GPIO.HIGH)

def update(angle):
	duty = float(angle) / 10.0 + 2.5
	print 'angle %d, duty %f' % (angle, duty)
	pwm.ChangeDutyCycle(duty)

update(90)
while True:
	angle = float(raw_input('angle : '))
	if angle == -1:
		break
	update(angle)

GPIO.cleanup()
