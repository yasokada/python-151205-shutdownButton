#!/usr/bin/env python

'''
v0.1  2015/12/05
  - add shutdown feature
'''

import RPi.GPIO as GPIO
import time
import os

swio=37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(swio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

chk1=GPIO.HIGH
chk2=GPIO.HIGH
chk3=GPIO.HIGH
while True:
	chk1=chk2
	chk2=chk3
	chk3=GPIO.input(swio)
	#print GPIO.input(swio)
	if chk1==GPIO.HIGH and chk2==GPIO.LOW and chk3==GPIO.LOW:
		print "start shutdown"
		os.system("/sbin/shutdown -h now")

	time.sleep(0.3)

