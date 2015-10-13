#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)

pwm_led = GPIO.PWM(pin, 500)
pwm_led.start(0)

for step in range(10):
	pwm_led.ChangeDutyCycle(step * 10)
	time.sleep(0.5)

for step in range(11):
	pwm_led.ChangeDutyCycle((10 - step) * 10)
	time.sleep(0.5)

GPIO.cleanup()
