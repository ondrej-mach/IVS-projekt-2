import math_library
from PyQt5 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """Binds the keys to the buttons on the screen

        Initializes main window object.
        It loads the layout from ui file.
        Then it sets keyboard shortcuts and shows the window.
        """
        super().__init__()
        self.setWindowTitle('Calculator')
        uic.loadUi('calculator.ui', self)
        self.setShortcuts()

        self.resultBox.setText('Hello There') # delete later TODO
        self.show()

    def setShortcuts(self):
        """Binds the keys to the buttons on the screen

        """
        # using QShortcut to bind more keys to one button
        # tuples of button and set of extra shortcuts
        extraShortcuts = [
            (self.pushButtonEvaluate, ['Enter', 'Return']),
            (self.pushButtonDecimalPoint, [',']),
        ]
        for button, keys in extraShortcuts:
            for key in keys:
                shortcut = QtWidgets.QShortcut(key, button)
                shortcut.activated.connect(button.animateClick)

        # bind all the buttons to their keys
        buttons = self.findChildren(QtWidgets.QPushButton)
        print(f'All buttons: {buttons}')

        for button in buttons:
            shortcut = button.text()
            button.setShortcut(shortcut)



app = QtWidgets.QApplication([])
window = MainWindow()

app.exec_()
