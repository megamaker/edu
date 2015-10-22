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

while True:
	statusFile = open('status.dat', 'r')
	status = int(statusFile.readline().strip())
	statusFile.close()

	if status:
		speedFile = open('speed.dat', 'r')
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

		directFile = open('direct.dat', 'r')
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

		statusFile = open('status.dat', 'w')
		statusFile.write('0')
		statusFile.close()

	time.sleep(0.5)
