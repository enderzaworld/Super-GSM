#!/usr/bin/env python
from gpiozero import Motor
#from time import sleep
MotorPinTopLeft1 = 5 #<--
MotorPinTopLeft2 = 6 #<--
MotorPinBottomLeft1 = 24 
MotorPinBottomLeft2 = 23 

MotorPinTopRight1 = 19 #<--
MotorPinTopRight2 = 26 #<--
MotorPinBottomRight1 = 16
MotorPinBottomRight2 = 13
#MotorEnable = 6
# new Wheel(enmWheel.TopLeft, 22, 27),
# new Wheel(enmWheel.TopRight, 12, 13),
# new Wheel(enmWheel.BottomLeft, 24, 23),
# new Wheel(enmWheel.BottomRight, 16, 26)
def setup():
	motorTopLeft = Motor(MotorPinTopLeft1, MotorPinTopLeft2)
	motorBottomLeft = Motor(MotorPinBottomLeft1, MotorPinBottomLeft2)
	
	motorTopRight = Motor(MotorPinTopRight1, MotorPinTopRight2)
	motorBottomRight = Motor(MotorPinBottomRight1, MotorPinBottomRight2)

def rForward():
	motorTopRight.forward()
	motorBottomRight.forward()

def lForward():
	motorTopLeft.forward()
	motorBottomLeft.forward()
	
def rBackward():
	motorTopRight.backward()
	motorBottomRight.backward()

def lBackward():
	motorTopLeft.backward()
	motorBottomLeft.backward()
	
def rStop():
	motorTopRight.stop()
	motorBottomRight.stop()

def lStop():
	motorTopLeft.stop()
	motorBottomLeft.stop()
	
def loop():
	while True:
		print 'Press Ctrl+C to end the program...'
		file = open("test.txt", "r")
		numState = file.read()
		print numState
		if numState == "0":
			rStop()
			lStop()
		if numState == "1":
			rForward()
			lStop()
		if numState == "2":
			rForward()
			lForward()
		if numState == "3":
			rStop()
			lForward()
		if numState == "4":
			rForward()
			lBackward()
		if numState == "5":
			rBackward()
			lForward()
		if numState == "6":
			rBackward()
			lStop()
		if numState == "7":
			rBackward()
			lBackward()
		if numState == "8":
			rStop()
			lBackward()
		
def destroy():
	rStop() # motor stop
	lStop()

if __name__ == '__main__': # Program start from here
	setup()
try:
	loop()
except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
	destroy()