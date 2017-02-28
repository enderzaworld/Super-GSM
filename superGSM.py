import serial
from time import sleep
con = False
while con==False:
	try:
		ser = serial.Serial('/dev/ttyUSB0', 38400)
		con = True
		print("connected")
	except Exception:
		print("waiting for device")
		sleep(1)
def loop():
	while True:
		print 'Press Ctrl+C to end the program...'
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
			ser.write(sendStr)
		#di pa sigurado ang nasa ibaba
		if ser.readline() == "addToken":
			nextLineNum = ser.readline();
			file2 = open("home/pi/addToken.txt", "rw+")
			file.truncate()
			file.write(nextLineNum)
			file.close()
		#print(ser.readline())
		sleep(1)
try:
	loop()
except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
	ser.readline()
# home/pi/addToken.txt ->10 #sample