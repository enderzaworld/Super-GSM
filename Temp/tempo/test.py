import serial

ser = serial.Serial('/dev/ttyUSB0', 38400)

def destroy():
        ser.readline()
def loop():
    while True:
        print(ser.readline())

try:
    loop()
except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
    destroy()
