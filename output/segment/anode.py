#!/usr/bin/env python
#encoding=utf-8

# anode 3 digit 7 segment
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

digit1 = 17
digit2 = 27
digit3 = 22
a = 18
b = 23
c = 24
d = 25
e = 12
f = 16
g = 20
dp = 21

digits = [digit1, digit2, digit3]
leds = [a, b, c, d, e, f, g, dp]
for pin in digits + leds:
	GPIO.setup(pin, GPIO.OUT)

def initDigit(data):
	digitStatus = map(int, data)
	for idx, digit in enumerate(digitStatus):
		if digit: GPIO.output(digits[idx], GPIO.HIGH)
		else: GPIO.output(digits[idx], GPIO.LOW)

def initLed(data):
	ledStatus = map(int, data)
	for idx, digit in enumerate(ledStatus):
		if digit: GPIO.output(leds[idx], GPIO.LOW)
		else: GPIO.output(leds[idx], GPIO.HIGH)

def num2bin(num):
	if num == 0: initLed('11111100')
	elif num == 1: initLed('01100000')
	elif num == 2: initLed('11011010')
	elif num == 3: initLed('11110010')
	elif num == 4: initLed('01100110')
	elif num == 5: initLed('10110110')
	elif num == 6: initLed('10111110')
	elif num == 7: initLed('11100000')
	elif num == 8: initLed('11111110')
	elif num == 9: initLed('11110110')

def numDisplay(num):
	if num < 10:
		initDigit('001')
		num2bin(num)
	elif num < 100:
		initDigit('010')
		num2bin(int(str(num)[0]))
		time.sleep(0.01)
		initDigit('001')
		num2bin(int(str(num)[1]))
		time.sleep(0.01)
	elif num > 99 and num < 1000:
		initDigit('100')
		num2bin(int(str(num)[0]))
		time.sleep(0.005)
		initDigit('010')
		num2bin(int(str(num)[1]))
		time.sleep(0.005)
		initDigit('001')
		num2bin(int(str(num)[2]))
		time.sleep(0.005)

try:
	while True:
		numDisplay(273)
except KeyboardInterrupt:
	GPIO.cleanup()
