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
	duty = float(angle + 90) / 10.0 + 2.5
	print 'angle %d, duty %f' % (angle, duty)
	pwm.ChangeDutyCycle(duty)

f = open('servoAngle', 'w')
f.write('0')
f.close()
time.sleep(0.5)

while True:
	f = open('servoStatus', 'r')
	status = int(f.readline().strip())
	f.close()

	if status:
		print status
		f = open('servoAngle', 'r')
		angle = int(f.readline().strip())
		f.close()
		print angle
		update(angle)

		f = open('servoStatus', 'w')
		f.write('0')
		f.close()

	time.sleep(0.5)
