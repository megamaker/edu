#!/usr/bin/env python

import time
import Adafruit_DHT

sensor = 11 # DHT11 (RHT01)
pin = 18

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	print 'Temp={0:0.1f} Humidity={1:0.1f}'.format(temperature, humidity)
	time.sleep(1)
