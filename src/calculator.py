import math_library as mlib
from PyQt5 import QtWidgets, uic
#  to copy lambda functions
from functools import partial
import enum

from os import path
import sys

# After packing everything into one executable, we have to find the ui file
bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
path_to_ui = path.abspath(path.join(bundle_dir, 'calculator.ui'))


class Workspace:
    class State(enum.Enum):
        TAKING_FIRST = 1
        TAKING_SECOND = 2
        SHOWING_RESULT = 3

    def __init__(self, printFn):
        self.state = self.State.TAKING_FIRST
        self.operands = ['', '']
        self.operator = ''
        self.printFn = printFn

    def readNew(self, symbol):
        # finite state machine
        operators = list(("+", "-", "*", "/", "!", "r", "^", "a", "l", "s", "c", "t"))

        if self.state == self.State.TAKING_FIRST:
            if symbol == '=':
                pass

            elif symbol in operators:
                self.operator = symbol
                self.state = self.State.TAKING_SECOND

            else:
                self.operands[0] += str(symbol)

        elif self.state == self.State.TAKING_SECOND:
            if symbol == '=':
                self.compute()
                self.state = self.State.SHOWING_RESULT

            elif symbol in operators:
                self.operator = symbol

            else:
                self.operands[1] += str(symbol)

        elif self.state == self.State.SHOWING_RESULT:
            if symbol == '=':
                pass

            elif symbol in operators:
                self.operator = symbol
                self.state = self.State.TAKING_SECOND

            else:
                self.state = self.State.TAKING_FIRST
                self.operands[0] = str(symbol)

        else:
            raise Exception('Cannot calculate')

        self.show()

    def compute(self):
        op0 = float(self.operands[0])
        op1 = float(self.operands[1])

        if self.operator == '+':
            result = mlib.add(op0, op1)

        elif self.operator == '-':
            result = mlib.subtract(op0, op1)

        elif self.operator == '*':
            result = mlib.multiply(op0, op1)

        elif self.operator == '/':
            result = mlib.divide(op0, op1)

        elif self.operator == '!':
            result = mlib.factorial(op0)

        elif self.operator == 'r':
            result = mlib.root(op1, op0)

        elif self.operator == '^':
            result = mlib.exponentiate(op0, op1)

        elif self.operator == 'a':
            result = mlib.absolute(op0)

        elif self.operator == 'l':
            result = mlib.logarithm(op0, op1)

        elif self.operator == 's':
            result = mlib.sine(op0)

        elif self.operator == 'c':
            result = mlib.cosine(op0)

        elif self.operator == 't':
            result = mlib.tangent(op0)

        else:
            raise Exception('Unknown operator')

        result = round(result, 6)

        # if result.is_integer():
        #    result = int(result)

        self.operands = [str(result), '']
        self.operator = ''

    def show(self):
        printedOperator = self.operator

        if printedOperator == 'r':
            printedOperator = '√'

        elif printedOperator == '/':
            printedOperator = '÷'

        elif printedOperator == 's':
            printedOperator = 'sin'

        elif printedOperator == 'c':
            printedOperator = 'cos'

        elif printedOperator == 't':
            printedOperator = 'tg'

        elif printedOperator == 'l':
            printedOperator = 'log'


        self.printFn(f'{self.operands[0]} {printedOperator} {self.operands[1]}')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """Binds the keys to the buttons on the screen

        Initializes main window object.
        It loads the layout from ui file.
        Then it sets keyboard shortcuts and shows the window.
        """
        super().__init__()
        #self.setWindowTitle('Calculator')
        uic.loadUi(path_to_ui, self)

        # print function is the argument of constructor
        self.workspace = Workspace(self.resultBox.setText)

        self.setShortcuts()
        self.setActions()

        self.show()

    # pretty much fully working, solid code
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

        noShortcuts = [
            self.pushButtonExponent,
            self.pushButtonRoot,
            self.pushButtonFactorial,
        ]

        for removedButton in noShortcuts:
            buttons.remove(removedButton)

        for button in buttons:
            shortcut = button.text()
            button.setShortcut(shortcut)

    # this might need to be rewritten
    def setActions(self):
        """Binds the keys to the buttons on the screen
        """
        buttons = self.findChildren(QtWidgets.QPushButton)

        specialButtons = [
            (self.pushButtonExponent, '^'),
            (self.pushButtonRoot, 'r'),
            (self.pushButtonFactorial, '!'),
            (self.pushButtonSinus, 's'),
        ]

        for button, symbol in specialButtons:
            buttons.remove(button)
            fnPartial = partial(lambda s: self.workspace.readNew(s), s=symbol)
            button.clicked.connect(fnPartial)

        for button in buttons:
            symbol = button.text()
            fnPartial = partial(lambda s: self.workspace.readNew(s), s=symbol)
            button.clicked.connect(fnPartial)


app = QtWidgets.QApplication([])
window = MainWindow()

app.exec_()
