#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------
# Project:  AMSpi class
# Author:   Jan Lipovský, 2016
# E-mail:   janlipovsky@gmail.com
# Licence:  MIT
# Description: Example of usage ASMpi class
# ---------------------------------------------

from AMSpi import AMSpi
import time
from time import sleep

if True:#__name__ == '__main__':
    # Calling AMSpi() we will use default pin numbering: BCM (use GPIO numbers)
    # if you want to use BOARD numbering do this: "with AMSpi(True) as amspi:"
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)
		
        while True:
            print ('Press Ctrl+C to end the program...')
            file = open("/home/pi/test.txt", "r")
            numState = file.read()
            print (numState)
            if numState == "0":
                    print("Stop")
                    amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
            if numState == "1":
                    print("Turn left")
                    amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4])
            if numState == "2":
                    print("Forward March")
                    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2], clockwise=False)
                    amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4])
            if numState == "3":
                    print("Turn right")
                    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2], clockwise=False)
            if numState == "4":
                    print("GO: counterclockwise")
                    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
                    amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4])
            if numState == "5":
                    print("GO: clockwise")
                    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2], clockwise = False)
                    amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4], clockwise=False)
            if numState == "6":
                    print("Turn left back")
                    amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4], clockwise=False)
            if numState == "7":
                    print("Retreat")
                    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
                    amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4], clockwise=False)
            if numState == "8":
                    print("Turn right back")
                    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
            sleep(0.1)

##print("GO: clockwise")
##amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
##time.sleep(2)

# print("Stop")
# amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
# time.sleep(1)

# print("GO: counterclockwise")
# amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4], clockwise=False)
# time.sleep(2)

# print("Stop")
# amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
# time.sleep(1)

# print("Turn right")
# amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_3])
# amspi.run_dc_motors([amspi.DC_Motor_2, amspi.DC_Motor_4], clockwise=False)
# time.sleep(1)

# print("Stop")
# amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
# time.sleep(1)

# print("Turn left")
# amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_3], clockwise=False)
# amspi.run_dc_motors([amspi.DC_Motor_2, amspi.DC_Motor_4])
# time.sleep(1)

# print("Stop and Exit")
# amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
