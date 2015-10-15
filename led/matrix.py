#!/usr/bin/env python
#encoding=utf-8

import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
row = [18, 23]
col = [16, 20, 21]
patterns1 = [
[ [1, 0, 0], 
  [0, 0, 0] ],
[ [0, 1, 0], 
  [0, 0, 0] ],
[ [0, 0, 1], 
  [0, 0, 0] ],
[ [0, 0, 0], 
  [0, 0, 1] ],
[ [0, 0, 0], 
  [0, 1, 0] ],
[ [0, 0, 0], 
  [1, 0, 0] ],
[ [0, 0, 0], 
  [0, 1, 0] ],
[ [0, 0, 0], 
  [0, 0, 1] ],
[ [0, 0, 1], 
  [0, 0, 0] ],
[ [0, 1, 0], 
  [0, 0, 0] ],
[ [1, 0, 0], 
  [0, 0, 0] ]
]
patterns2 = [
[ [1, 0, 0], 
  [0, 0, 0] ],
#[ [0, 1, 0], 
#  [0, 0, 0] ],
[ [0, 0, 1], 
  [0, 0, 0] ],
#[ [0, 0, 0], 
#  [0, 0, 1] ],
[ [0, 0, 0], 
  [0, 1, 0] ],
#[ [0, 0, 0], 
#  [1, 0, 0] ]
]

def display(pattern):
	for rpin in row:
		GPIO.output(rpin, GPIO.LOW)

	for rIndex in range(len(pattern)):
		if 1 in pattern[rIndex]:
			GPIO.output(row[rIndex], GPIO.HIGH)

			for cIndex in range(len(pattern[rIndex])):
				if pattern[rIndex][cIndex]:
					GPIO.output(col[cIndex], GPIO.LOW)
				else:
					GPIO.output(col[cIndex], GPIO.HIGH)

for pin in row:
	GPIO.setup(pin, GPIO.OUT)
for pin in col:
	GPIO.setup(pin, GPIO.OUT)

for pin in row:
	GPIO.output(pin, GPIO.LOW)
for pin in col:
	GPIO.output(pin, GPIO.HIGH)

if sys.argv[1] == "1":
	while True:
		for pattern in patterns1:
			display(pattern)
			time.sleep(0.1)
if sys.argv[1] == "2":
	while True:
		for pattern in patterns2:
			display(pattern)
			time.sleep(0.002)

GPIO.cleanup()
