# This Python file uses the following encoding: utf-8
import sys
import math
#from PySide2.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow


class InputPage(QMainWindow):
    def __init__(self):
        super(InputPage, self).__init__()
        loadUi('GUI.ui', self)
        self.pushButtonGenerate.clicked.connect(self.input_data_GUI)
        self.pushButtonGenerate.clicked.connect(self._3d_scan)

#        self.pushButtonGenerate.clicked.connect(self.loop_xaxis)
#        self.pushButtonGenerate.clicked.connect(self.complete_horizontal_slice)

    def input_data_GUI(self):
        # Input values
        self.xAxisLength = int(math.ceil(self.xLength.value()))
        self.xAxisRes = int(self.xRes.value())
        self.zAxisLength = float(self.zLength.value())
        self.zAxisRes = float(self.zRes.value())
        self.sensorDelay = int(self.sensorDelay.value()/100)
        self.rotationRes = float(self.rotationRes.value()/2)
        # convert input values
        zLayers = float(math.ceil(self.zAxisLength/self.zAxisRes))  # round up to nearest whole layer
        zHeight = self.zAxisRes*zLayers                    # find what height to use in loop
        # Seperate whole numbers and decimals to be able to loop
        self.zHeight = int(math.floor(zHeight))
        self.z_decimal = round((float(zHeight-self.zHeight)), self.zLength.decimals())
        self.zResolution = int(math.floor(self.zAxisRes))
        self.zRes_decimal = round((float(self.zAxisRes-self.zResolution)), self.zRes.decimals())

    def _3d_scan(self):
        zRes_decimal = round(self.zRes_decimal, 2)    # to have a variable that can increase the steps in resolution
        for j in range(1, self.zHeight+1, self.zResolution):
            j += zRes_decimal
            if j > self.zHeight:
                print("G1 Z", "%.2f" % j, " Y", "%.2f" % j, "   ; LAYER SHIFT", sep='')
                break
#            self.complete_horizontal_slice()
            print("G1 Z", "%.2f" % j,  " Y",  "%.2f" % j, "      ; LAYER SHIFT",  sep='')
            zRes_decimal += self.zRes_decimal

    # movement for getting a full 2d slice in xy-plane

    def complete_horizontal_slice(self):
        e = self.rotationRes
        e1 = 2
        for i in range (1, 10, 1):                             # Since 1.125 is added two times per round in this loop,  80 loops equals 160 rotational movements
            self.x_axis_forward()            # Runs the function,  return the value from that function and assign it as y
        #        print("G4 P200.0")
            print("T0")
            print("G92 E0")
            print("G1 E", e,  "       ; ROTATE",  sep='')
    #        e1 += 2
            print("T1")
            print("G92 E0")
            print("G1 E",  e1,  sep='')            # Move E axis to trigger sensor readings
            self.x_axis_backward()              # Uses y as an argument an runs the function
        #        print("G4 P200.0")
    #        e += 1.125  #0.5
            print("T0")
            print("G92 E0")
            print("G1 E", e, "        ; ROTATE",  sep='')
        #        print("G4 P200.0")
    #        e += 1.125  #0.5
        return e

    def x_axis_forward(self):
        print(self.xAxisLength)
        print("T1")
        print("G92 E0")
        x = 0.4                                 # variable to compensate for lack of float numbers in a "range" function
        e1 = 2                                  # 1= 100ms. Starts at e1 = 2mm because the first activation of sensor reading needs to happen before the first movement of x
        print("G1 E", e1, sep='')                # Move E axis to trigger sensor readings
    #    delay = 150.0                           # delay before next movement in milliseconds
        e1 += 2
        for i in range(0, self.xAxisLength, 25):
            if (i == 0):
                continue
            else:
                i += x
            if i > 203.2:
                break
            if (i == 203.2):
                print("G1 X", i, sep='')
            else:
                print("G1 X", i, sep='')
            if (i == 203.2):
                print("G1 E", e1, sep='')            # Move E axis to trigger sensor readings
                break
            else:
                # print("G4 P",  delay, sep='')
                print("G1 E", e1, sep='')        # Move E axis to trigger sensor readings
            x += 0.4
            e1 += 2
        self.xAxisReturn = i
        self.decimal = round((self.xAxisReturn-int(self.xAxisReturn)), 1)
        print(self.decimal)
    #    return e1                                # Returns the value of y,  to be used in another function



    def x_axis_backward(self):
    #    print("T1")
        x = -(-0.4 + self.decimal)
    #    print("G1 E", e1, sep='')            # Move E axis to trigger sensor readings
    #    e1 -= 2
        e1 = 2
    #    delay = 150.0                           # delay before next movement in milliseconds
        for i in range(203, 0, -25):
            i -= x
            if i >= 200:
                continue
            if (i < 25.4):
                print ("G1 X0")
                print("G1 E", e1, sep='')            # Move E axis to trigger sensor readings
                break
            print("G1 X", i, sep='')
            # print("G4 P",  delay, sep='')
            print("G1 E", e1, sep='')            # Move E axis to trigger sensor readings
            x += 0.4
            e1 += 2



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputPage()
    print("test")
    window.show()
    sys.exit(app.exec_())
