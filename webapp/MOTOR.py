#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Motor1A = 23
Motor1B = 24
Motor1E = 25

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.output(Motor1E, GPIO.HIGH)
pwm = GPIO.PWM(Motor1E, 500)
pwm.start(0)

def func(direct, speed):
	if direct == 'S':
		pwm.ChangeDutyCycle(0)
		GPIO.output(Motor1A, GPIO.HIGH)
		GPIO.output(Motor1B, GPIO.HIGH)
	elif direct == 'F':
		GPIO.output(Motor1A, GPIO.HIGH)
		GPIO.output(Motor1B, GPIO.LOW)
	elif direct == 'B':
		GPIO.output(Motor1B, GPIO.HIGH)
		GPIO.output(Motor1A, GPIO.LOW)
	if speed == '1':
		pwm.ChangeDutyCycle(25)
	elif speed == '2':
		pwm.ChangeDutyCycle(60)
	elif speed == '3':
		pwm.ChangeDutyCycle(100)

while True:
	f = open('status.dat', 'r')
	status = int(f.readline().strip())
	f.close()

	if status:
		print status
		f = open('direct.dat', 'r')
		direct = f.readline().strip()
		f.close()
		print direct
		f = open('speed.dat', 'r')
		speed = f.readline().strip()
		f.close()
		print speed
		f = open('status.dat', 'w')
		f.write('0')
		f.close()
		func(direct, speed)
	
	time.sleep(0.5)
