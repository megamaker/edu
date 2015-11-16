#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

motor = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor, GPIO.OUT)
pwm = GPIO.PWM(motor, 100)
pwm.start(2.5)

def update(angle):
	duty = float(angle) / 10.0 + 2.5
	print 'angle %d, duty %f' % (angle, duty)
	pwm.ChangeDutyCycle(duty)

try:
	while True:
		for angle in [20, 45, 90, 150, 200, 150, 90, 45]:
			update(angle)
			time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
