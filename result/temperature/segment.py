#!/usr/bin/env python

import time
import re
import Adafruit_DHT
import RPi.GPIO as GPIO

sensor = 11 # DHT11 (RHT01)
pinSensor = 18

digit1 = 24 # 12
digit2 = 26 # 9
digit3 = 21 # 8
pinA = 23 # 11
pinB = 20 # 7
pinC = 12 # 4
pinD = 8 # 2
pinE = 25 # 1
pinF = 22 # 10
pinG = 16 # 5
pinDP = 7 # 3
pinBtn = 27

GPIO.setmode(GPIO.BCM)
digits = [digit1, digit2, digit3]
segments = [pinA, pinB, pinC, pinD, pinE, pinF, pinG, pinDP]

GPIO.setup(pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in digits + segments:
	GPIO.setup(pin, GPIO.OUT)

def initDigit(data):
	digitStatus = map(int, data)
	for idx, digit in enumerate(digitStatus):
		if digit: GPIO.output(digits[idx], GPIO.HIGH)
		else: GPIO.output(digits[idx], GPIO.LOW)

def initLed(data):
	ledStatus = map(int, data)
	for idx, digit in enumerate(ledStatus):
		if digit: GPIO.output(segments[idx], GPIO.LOW)
		else: GPIO.output(segments[idx], GPIO.HIGH)

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
	refresh = 0
	temperature = 0
	humidity = 0
	while True:
		if refresh == 0:
			numDisplay(0)
			humidity, temperature = Adafruit_DHT.read_retry(sensor, pinSensor)
			print 'Temp={0:0.1f} Humidity={1:0.1f}'.format(temperature, humidity)

		if GPIO.input(pinBtn): numDisplay(int(temperature))
		else: numDisplay(int(humidity))

		refresh += 1
		if refresh == 100: refresh = 0
except KeyboardInterrupt:
	GPIO.cleanup()
