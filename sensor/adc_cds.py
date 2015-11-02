#!/usr/bin/env python

import RPi.GPIO as GPIO
import spidev
import time

ledPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)

def analog_read(channel):
	r = spi.xfer2([1, (8 + channel) << 4, 0])
	adc_out = ((r[1]&3) << 8) + r[2]
	return adc_out

try:
	while True:
		reading = analog_read(0)
		voltage = reading * 3.3 / 1024
		print 'Reading=%d\tVoltage=%f' % (reading, voltage)
		if voltage < 1:
			GPIO.output(ledPin, GPIO.HIGH)
		else:
			GPIO.output(ledPin, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.output(ledPin, GPIO.LOW)
