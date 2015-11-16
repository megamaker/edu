#!/usr/bin/env python
#encoding=utf-8

# anode 3 digit 7 segment
import RPi.GPIO as GPIO
import time
import re

GPIO.setmode(GPIO.BCM)

# pin mapping
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

def num2bin(num, pointStatus=0):
	ledNums = {0:'11111100', 1:'01100000', 2:'11011010', 3:'11110010', 4:'01100110', 5:'10110110', 6:'10111110', 7:'11100000', 8:'11111110', 9:'11110110'}
	ledNum = ''
	if num == 0: ledNum = ledNums[0]
	elif num == 1: ledNum = ledNums[1]
	elif num == 2: ledNum = ledNums[2]
	elif num == 3: ledNum = ledNums[3]
	elif num == 4: ledNum = ledNums[4]
	elif num == 5: ledNum = ledNums[5]
	elif num == 6: ledNum = ledNums[6]
	elif num == 7: ledNum = ledNums[7]
	elif num == 8: ledNum = ledNums[8]
	elif num == 9: ledNum = ledNums[9]

	if pointStatus:
		ledNum = str(int(ledNum) + 1)

	initLed(ledNum)

def numDisplay_func(digit, num, sleep):
	initDigit(digit)
	num2bin(int(str(num)[idx]), 
	

def numDisplay(num):
	if re.search(r'\.', str(num)):
		if num < 10:
			initDigit('010')
			num2bin(int(str(num)[0]), 1)
			time.sleep(0.01)
			initDigit('001')
			num2bin(int(str(num)[2]))
			time.sleep(0.01)
		elif num < 100:
			initDigit('100')
			num2bin(int(str(num)[0]))
			time.sleep(0.005)
			initDigit('010')
			num2bin(int(str(num)[1]), 1)
			time.sleep(0.005)
			initDigit('001')
			num2bin(int(str(num)[3]))
			time.sleep(0.005)
	else:
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
		numDisplay(5.64)
except KeyboardInterrupt:
	GPIO.cleanup()
