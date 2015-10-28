#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

pin18 = 18
pin16 = 16
pin20 = 20
pin21 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin18, GPIO.HIGH)
GPIO.setup(pin16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin20, GPIO.IN)
GPIO.setup(pin21, GPIO.IN)

while True:
	if GPIO.input(16):
		print 'input'

#RPWM = GPIO.PWM(pin16, 100)
#RPWM.start(0)
#GPWM = GPIO.PWM(pin20, 100)
#GPWM.start(0)
#BPWM = GPIO.PWM(pin21, 100)
#BPWM.start(0)

#for step in range(10):
#	RPWM.ChangeDutyCycle(float(step * 10))
#	time.sleep(0.3)

#time.sleep(1)
#GPIO.cleanup()
