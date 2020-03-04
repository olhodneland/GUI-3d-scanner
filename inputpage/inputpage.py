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
        self.pushButtonGenerate.clicked.connect(self.loop_x_axis)
#        self.pushButtonGenerate.clicked.connect(self.x_axis_backward_section_w_delay)

    def input_data_GUI(self):
        self.xAxisLength = int(math.ceil(self.xLength_2.value()))
        self.sensorDelay = int(self.sensorDelay_2.value()/100)

    def loop_x_axis(self):
        for i in range(1, 5, 1):
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

#    def complete_horizontal_slice(self, x_axis_forward_section_w_delay, ):
#        global e
#        e1 = 2
#        for i in range(1, 2, 1):                             # Since 1.125 is added two times per round in this loop,  80 loops equals 160 rotational movements
#            x_axis_forward_section_w_delay(self)            # Runs the function,  return the value from that function and assign it as y
#        #        print("G4 P200.0")
#            print("T0")
#            print("G92 E0")
#            print("G1 E", e,  "       ; ROTATE", sep='')
#    #        e1 += 2
#            print("T1")
#            print("G92 E0")
#            print("G1 E",  e1, sep='')            # Move E axis to trigger sensor readings
#            x_axis_backward_section_w_delay(self)              # Uses y as an argument an runs the function
#        #        print("G4 P200.0")
#    #        e += 1.125  #0.5
#            print("T0")
#            print("G92 E0")
#            print("G1 E", e, "        ; ROTATE", sep='')
#        #        print("G4 P200.0")
#    #        e += 1.125  #0.5
#        return e

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputPage()
    print("test")
    window.show()
    sys.exit(app.exec_())
