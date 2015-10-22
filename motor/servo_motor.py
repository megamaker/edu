#!/usr/bin/env python
#encoding=utf-8

import RPi.GIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor = 18

GPIO.setup(motor, GPIO.OUT)
pwm = GPIO.PWM(motor, 100)
pwm.start(0)

#GPIO.output(motor, GPIO.HIGH)

def update(angle):
	duty = float(angle) / 10.0 + 2.5
	pwm.ChangeDutyCycle(duty)

while True:
	angle = int(raw_input('angle : '))
	if angle == -1:
		break
	update(angle)

GPIO.cleanup()
