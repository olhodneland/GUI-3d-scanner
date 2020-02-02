#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Thu Dec 13 14:18:18 2018
#
#@author: oyvindlundehodneland
#""" 

#what is the things we need
#M92: Sets steps per mm
#G-codes used:
# G1: movement
#G1 F3000: speed
#G28: Home all axsis
#M302 P1: Allow cold extrusion / allow E0 to move
#G4 P101: "Dwell" pauses everything in P milliseconds
#M204: Set start acceleration

#scanning area in mm
maxHeight = 3
maxWidth = 250
minWidth = 0
maxRotation = 200 
minRotation = 0   
positionRotation = 50       # 360 degrees = 200mm

#Positions 
sectionMovementXcarrige = 25 # in mm. How much the carrige should move after each reading from sensor
heightPosition = 0         # y & z motors
newHeightPosition = 0
horizontalPosition = 0     # X - motor
lastX = 0
rotationPisition = 0
lastRotationPosition = 0        # E0 - motor
lastE0 = 0

#Speed
xSpeed = 27500
generalSpeed = 4000
Accel = 10000

#Resolution
resolutionHeight = 1
resolutionRotation = 50
resolutionRotationSteps = 50   
resolutionHorizontal = 25.4  

#timing
xAxisDelay = 101  # milliseconds
#Homing
print("M302 P1") #allow cold extrusions/ allow E0 to move
print("G28")
print("G1 F3000")
print("M92 E16")    #set steps/mm E0

#########  HEIGHT    ############
for i in range(heightPosition,(maxHeight+resolutionHeight),resolutionHeight):
    print("############ Z-POSITION = ","%0.2f" %heightPosition,"  ############", sep= '' )
    if heightPosition>0:
        print("G1 Z","%0.2f" %heightPosition, sep= '', end='')
        print(" Y", "%0.2f" %heightPosition, " F","%0.2f" %generalSpeed, sep= '')
    heightPosition = heightPosition + resolutionHeight
    print("M204 T",Accel, sep= '')
    print("G1 F",xSpeed, sep= '')
############        Horizontal ########
    for j in range (0,maxRotation,resolutionRotationSteps):
        if (horizontalPosition == 0):
            for k in range (0, maxWidth,sectionMovementXcarrige ):
                horizontalPosition = horizontalPosition + resolutionHorizontal
                print("G4 P","%0.2f" %xAxisDelay, sep= '')
                print("G1 X","%0.2f" %horizontalPosition, sep= '')
                if (horizontalPosition > maxWidth):
                    horizontalPosition = maxWidth
        print("ROTATION !")
        print("G1 E", "%0.2f" %positionRotation, " F",generalSpeed, sep= '')
        print("M204 T",Accel, sep= '')
        print("G1 F",xSpeed, sep= '')
        positionRotation = positionRotation + resolutionRotation
        if(positionRotation <= minRotation or positionRotation >= maxRotation):
            resolutionRotation = -resolutionRotation
        if(horizontalPosition == maxWidth):
            for l in range (0, maxWidth,sectionMovementXcarrige ):
                horizontalPosition = horizontalPosition -  resolutionHorizontal
                print("G4 P","%0.2f" %xAxisDelay, sep= '')
                print("G1 X","%0.2f" %horizontalPosition, sep= '')
                
        print("ROTATION !")
        print("G1 E", "%0.2f" %positionRotation, " F",generalSpeed, sep= '')
        print("M204 T",Accel, sep= '')
        print("G1 F",xSpeed, sep= '')
        positionRotation = positionRotation + resolutionRotation
        if(positionRotation <= minRotation or positionRotation >= maxRotation):
            resolutionRotation = -resolutionRotation
    #############     ROTATION ##########           

print ("##### SCAN FINISHED ON HEIGHT = ", "%0.2f" %(heightPosition-resolutionHeight)," #########", sep= '')
print ("M18")