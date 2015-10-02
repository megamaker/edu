#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def led_on(LED_PIN):
	GPIO.setup(LED_PIN, GPIO.OUT)
	GPIO.output(LED_PIN, GPIO.HIGH)

def led_off(LED_PIN):
	GPIO.setup(LED_PIN, GPIO.OUT)
	GPIO.output(LED_PIN, GPIO.LOW)
