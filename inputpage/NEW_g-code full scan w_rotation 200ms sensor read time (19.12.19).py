#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:59:40 2019

@author: oyvindlundehodneland
"""

import sys
sys.stdout = open('/Users/oyvindlundehodneland/Desktop/TESTTESTEST.txt',  'w')          # Write all console output values to file,  at this location.
print("; FULL SCAN W_ROTATION,  200ms READ TIME SENSOR")
print("\n")

#######x-axis section movement


def  x_axis_forward_section_w_delay():
    print("T1")
    print("G92 E0")
    x = 0.4                                 # variable to compensate for lack of float numbers in a "range" function
    e1 = 2                                  # 1= 100ms. Starts at e1 = 2mm because the first activation of sensor reading needs to happen before the first movement of x
    print("G1 E", e1,  sep='')                # Move E axis to trigger sensor readings
#    delay = 150.0                           # delay before next movement in milliseconds
    e1 += 2
    for i in range (0, 250, 25):
        if (i == 0):
            continue
        else:
            i += x
        if i > 203.2:
            break
        if (i == 203.2):
            print("G1 X", i, sep= '')
        else:
            print("G1 X", i,  sep='')
        if (i == 203.2):
            print("G1 E", e1,  sep='')            # Move E axis to trigger sensor readings
            break
        else:
            # print("G4 P",  delay,  sep='')
            print("G1 E", e1,  sep='')        # Move E axis to trigger sensor readings
        x += 0.4
        e1 += 2
#    return e1                                # Returns the value of y,  to be used in another function


def  x_axis_backward_section_w_delay():
#    print("T1")
    x = 1.2
#    print("G1 E", e1,  sep='')            # Move E axis to trigger sensor readings
#    e1 -= 2
    e1 = 2
#    delay = 150.0                           # delay before next movement in milliseconds
    for i in range (204, 0, -25):
        i -= x
        if i >= 200:
            continue
        if (i < 25.4):
            print ("G1 X0")
            print("G1 E", e1,  sep='')            # Move E axis to trigger sensor readings
            break
        print("G1 X", i,  sep='')
        # print("G4 P",  delay,  sep='')
        print("G1 E", e1,  sep='')            # Move E axis to trigger sensor readings
        x += 0.4
        e1 += 2

####### movement for getting a full 2d slice in xy-plane
        
def complete_horizontal_slice():
    global e
    e1 = 2
    for i in range (1, 81, 1):                             # Since 1.125 is added two times per round in this loop,  80 loops equals 160 rotational movements
        x_axis_forward_section_w_delay()            # Runs the function,  return the value from that function and assign it as y
    #        print("G4 P200.0")
        print("T0")
        print("G92 E0")
        print("G1 E", e,  "       ; ROTATE",  sep='')
#        e1 += 2
        print("T1")
        print("G92 E0")
        print("G1 E",  e1,  sep='')            # Move E axis to trigger sensor readings
        x_axis_backward_section_w_delay()              # Uses y as an argument an runs the function
    #        print("G4 P200.0")
#        e += 1.125  #0.5
        print("T0")
        print("G92 E0")
        print("G1 E", e, "        ; ROTATE",  sep='')
    #        print("G4 P200.0")
#        e += 1.125  #0.5
    return e






################ MAIN PROGRAM #################
        
print("M914 X10         ; Set sensorless homing sensitivity to 10 for the x-axis")
print("G28              ; Home all axis")            # Home all axis
print("M204 T10000      ; Set the travel acceleration to 10000") 
print("G1 F6000         ; Set the travel speed to 6000 mm/min equals 100 mm/s")
print("M302 P1          ; Allow cold extrusions/ allow E0 to move")
print("G1 E0            ; 'Home' E axis")
print("G4 P500          ; Pause for 500 ms")
print("M92 E30          ; Change steps/mm on E-axis")
print("M92 E7.78       ; Change steps/mm on E-axis back. This is probably a bug in firmware. Need to be done to make the axis run smooth")
print("\n")
print("; PROGRAM START")


e = 1.125                             # one step on rotation. 1.125mm = 2, 25 degrees because 0.5mm = 1 degree
for j in range (2, 202, 2):             # number of layers
    complete_horizontal_slice()
    print("G1 Z",  j,  " Y",  j, "      ; LAYER SHIFT",  sep='')

print("\n")
print("; PROGRAM FINISH")
