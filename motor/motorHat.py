#!/usr/bin/env python

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import time

mh = Adafruit_MotorHAT(addr=0x60)
def turnOffMotors():
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)

motor3 = mh.getMotor(3)

time.sleep(3)

for speed in range(1,510):
	motor3.run(Adafruit_MotorHAT.FORWARD)
	if speed > 255: speed = 510 - speed
	motor3.setSpeed(speed)
	time.sleep(0.01)
for speed in range(1,510):
	motor3.run(Adafruit_MotorHAT.BACKWARD)
	if speed > 255: speed = 510 - speed
	motor3.setSpeed(speed)
	time.sleep(0.01)
