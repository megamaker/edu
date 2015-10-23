#!/usr/bin/env python

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import time

mh = Adafruit_MotorHAT(addr=0x60)
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)

motor3 = mh.getMotor(3)
motor4 = mh.getMotor(4)

path = '/home/pi/dev/src/webapp'
while True:
	statusFile = open('%s/status'%path, 'r')
	status = int(statusFile.readline().strip())
	statusFile.close()

	if status:
		speedFile = open('%s/speed'%path, 'r')
		speed = speedFile.readline().strip()
		speedFile.close()
		if speed == '1':
			motor3.setSpeed(85)
			motor4.setSpeed(85)
		if speed == '2':
			motor3.setSpeed(170)
			motor4.setSpeed(170)
		if speed == '3':
			motor3.setSpeed(255)
			motor4.setSpeed(255)

		directFile = open('%s/direct'%path, 'r')
		direct = directFile.readline().strip()
		directFile.close()
		if direct == 'F':
			motor3.run(Adafruit_MotorHAT.FORWARD)
			motor4.run(Adafruit_MotorHAT.FORWARD)
		if direct == 'B':
			motor3.run(Adafruit_MotorHAT.BACKWARD)
			motor4.run(Adafruit_MotorHAT.BACKWARD)
		if direct == 'S':
			motor3.run(Adafruit_MotorHAT.RELEASE)
			motor4.run(Adafruit_MotorHAT.RELEASE)
		if direct == 'L':
			motor3.run(Adafruit_MotorHAT.FORWARD)
			motor4.run(Adafruit_MotorHAT.BACKWARD)
		if direct == 'R':
			motor3.run(Adafruit_MotorHAT.BACKWARD)
			motor4.run(Adafruit_MotorHAT.FORWARD)

		statusFile = open('%s/status'%path, 'w')
		statusFile.write('0')
		statusFile.close()

	time.sleep(0.5)
