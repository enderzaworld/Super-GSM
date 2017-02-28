#!/usr/local/bin/python
from gpiozero import Motor
from gpiozero import LED
from time import sleep
#MotorEnable = 6
# new Wheel(enmWheel.TopLeft, 22, 27),
# new Wheel(enmWheel.TopRight, 12, 13),
# new Wheel(enmWheel.BottomLeft, 24, 23),
# new Wheel(enmWheel.BottomRight, 16, 26)
MotorPinTopLeft1 = 5 #<--
MotorPinTopLeft2 = 6 #<--
MotorPinTopRight1 = 19 #<--
MotorPinTopRight2 = 26 #<--

Pin1 = 16
Pin2 = 13
Pin3 = 24 
Pin4 = 23

pin1 = LED(Pin1)
pin2 = LED(Pin2)
pin3 = LED(Pin3)
pin4 = LED(Pin4)

motorTopLeft = Motor(MotorPinTopLeft1, MotorPinTopLeft2)
motorTopRight = Motor(MotorPinTopRight1, MotorPinTopRight2)

def rForward():
        motorTopRight.forward()
        pin1.on()
        pin2.on()
        pin3.on()
        pin4.on()
def lForward():
        motorTopLeft.forward()
        pin1.on()
        pin2.on()
        pin3.on()
        pin4.on()
def rBackward():
        motorTopRight.backward()
        pin1.on()
        pin2.on()
        pin3.on()
        pin4.on()
def lBackward():
        motorTopLeft.backward()
        pin1.on()
        pin2.on()
        pin3.on()
        pin4.on()
def rStop():
	motorTopRight.stop()

def lStop():
	motorTopLeft.stop()
	
def loop():
	while True:
		print ('Press Ctrl+C to end the program...')
		file = open("test.txt", "r")
		numState = file.read()
		print (numState)
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
        pin1.off()
        pin2.off()
        pin3.off()
        pin4.off()

#if True: #__name__ == '__main__': # Program start from here
#       setup()
belo = True
while belo:
        try:
                loop()
        except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
                destroy()
                belo = False
        sleep(0.1)
