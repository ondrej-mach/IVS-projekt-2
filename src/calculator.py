import math_library
import sys
from PyQt5 import QtWidgets, uic

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('calculator.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Window()
app.exec_()
