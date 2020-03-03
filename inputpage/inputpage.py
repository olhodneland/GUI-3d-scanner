# This Python file uses the following encoding: utf-8
import sys
#from PySide2.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow


class InputPage(QMainWindow):
    def __init__(self):
        super(InputPage, self).__init__()
        loadUi('GUI.ui', self)
        self.pushButtonGenerate.clicked.connect(self.x_axis_forward_section_w_delay)

    def x_axis_forward_section_w_delay(self):
        xAxisLength = int(self.xLength_2.value())
        sensorDelay = int(self.sensorDelay_2.value()/100)

        print(xAxisLength)
        print("T1")
        print("G92 E0")
        x = 0.4
        e1 = sensorDelay
        print("G1 E", e1, sep='')
        e1 += sensorDelay
        for i in range(0, xAxisLength, 25):
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
                print("G1 E", e1, sep='')
                break
            else:
                print("G1 E", e1, sep='')
            x += 0.4
            e1 += sensorDelay
        #    return e1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputPage()
    print("test")
    window.show()
    sys.exit(app.exec_())
