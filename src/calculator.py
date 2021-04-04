import math_library
import sys
from PyQt5 import QtWidgets, uic

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        """Binds the keys to the buttons on the screen

        Initializes main window object.
        It loads the layout from ui file.
        Then it sets keyboard shortcuts and shows the window.
        """
        super(Window, self).__init__()
        uic.loadUi('calculator.ui', self)
        self.setShortcuts()
        self.resultBox.setText('Hello There') # delete later TODO
        self.show()

    def setShortcuts(self):
        """Binds the keys to the buttons on the screen

        """
        # using QShortcut to bind more keys to one button
        for key in {'Enter', 'Return'}:
            shortcut = QtWidgets.QShortcut(key, self.pushButtonEvaluate)
            shortcut.activated.connect(self.pushButtonEvaluate.animateClick)

        self.pushButtonNumber0.setShortcut('0')
        self.pushButtonNumber1.setShortcut('1')
        self.pushButtonNumber2.setShortcut('2')
        self.pushButtonNumber3.setShortcut('3')
        self.pushButtonNumber4.setShortcut('4')
        self.pushButtonNumber5.setShortcut('5')
        self.pushButtonNumber6.setShortcut('6')
        self.pushButtonNumber7.setShortcut('7')
        self.pushButtonNumber8.setShortcut('8')
        self.pushButtonNumber9.setShortcut('9')

app = QtWidgets.QApplication(sys.argv)
window = Window()
app.exec_()
