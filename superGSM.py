import serial
from time import sleep
import os # Import the os library

usbState = True

charging = False

con = False
while con==False:
	try:
		ser = serial.Serial('/dev/ttyUSB0', 38400)
		con = True
		print("connected")
	except Exception:
		print("waiting for device")
		sleep(1)
def usbOff():
	if charging == False
		if usbState == True
			os.system("/etc/init.d/networking stop")
			os.system("echo 0 > /sys/devices/platform/bcm2708_usb/buspower;")
			usbState = False
def usbOn():
	if usbState == False
		os.system("echo 1 > /sys/devices/platform/bcm2708_usb/buspower;")
		os.system("sleep 2;")
		os.system("/etc/init.d/networking start")
		usbState = True
def loop():
	while True:
		print 'Press Ctrl+C to end the program...'
		file3 = open("home/pi/chargeState.txt", "rw+")
		chargeState = file3.read() #0 or 1
		file3.close()
		if chargeState == "1"
			charging = True
		else
			charging = False
		if charging == True:
			usbOn()
		else
			usbOff()
		file = open("home/pi/sendMsgTrigger.txt", "rw+")
		sendTrigger = file.read() #0 or 1
		if sendTrigger == "1":
			file.truncate()
			file.write("0")
			file.close()
			
			file1 = open("home/pi/sendMsg.txt", "rw+")
			sendStr = file1.read()
			file1.truncate()
			file1.close()
			usbOn()
			ser.write(sendStr)
		#di na sigurado ang nasa ibaba
		usbOn()
		ser.write("retrieve")
		not_valid = True
		waitcycle = 100
		number=0
		while not_valid:
			try:
				number = int(ser.readline())
				not_valid = False
			except:
				number = 0
			waitcycle = waitcycle-1
			#timeout
			if waitcycle <= 0:
				number = 0
				not_valid = False
		usbOff()
		if number > 0:
			file2 = open("home/pi/addToken.txt", "rw+")
			file2.truncate()
			file2.write(number)
			file2.close()
		sleep(1)
try:
	loop()
except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
	ser.readline()
# home/pi/addToken.txt ->10 #sample