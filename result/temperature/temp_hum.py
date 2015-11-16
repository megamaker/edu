#!/usr/bin/env python

import Adafruit_DHT
import time

sensor = 11 # DHT11 (RHT01)
pinSensor = 18

try:
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pinSensor)
		print 'Temp={0:0.1f} Humidity={1:0.1f}'.format(temperature, humidity)
		time.sleep(1)
except KeyboardInterrupt:
	pass
