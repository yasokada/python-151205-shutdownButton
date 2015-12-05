#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

swio=37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(swio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#for loop in range(0,10):
while True:
	print GPIO.input(swio)
	'''
	if GPIO.input(37) == GPIO.LOW:
		GPIO.output(33, True)
	else:
		GPIO.output(33, True)
	'''
	time.sleep(0.3)

