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
        self.firstOperand = ''
        self.firstOperand = ''
        self.secondOperand = ''
        self.operator = ''
        self.printFn = printFn

        self.unaryMap = {
            'a': mlib.absolute,
            'sin': mlib.sine,
            'cos': mlib.cosine,
            'tg': mlib.tangent,
            '!': mlib.factorial,
        }

        self.binaryMap = {
            '+': (mlib.add, False),
            '-': (mlib.subtract, False),
            '*': (mlib.multiply, False),
            '/': (mlib.divide, False),
            'r': (mlib.root, True),
            '^': (mlib.exponentiate, False),
            'log': (mlib.logarithm, True),
        }

        self.operatorMap = {
            'r': '√',
            '/': '÷',
            '*': '×',
        }

        self.operandMap = {
            'π': round(mlib.PI, 6),
            'e': round(mlib.E, 6),
        }

    def clear(self):
        self.operator = ''
        self.firstOperand = ''
        self.secondOperand = ''

    def readNew(self, symbol):
        # finite state machine
        binaryOperators = self.binaryMap.keys()
        unaryOperators = self.unaryMap.keys()

        if self.state == self.State.TAKING_FIRST:
            if symbol == '=':
                pass

            elif symbol == '-' and self.firstOperand == '':
                self.firstOperand = symbol

            elif symbol == 'C':
                self.clear()

            elif symbol == 'CE':
                if not self.operator == '':
                    self.operator = ''

                elif not self.firstOperand == '':
                    self.firstOperand = self.firstOperand[:-1]

            elif symbol in unaryOperators:
                if self.firstOperand == '':
                    pass
                else:
                    self.operator = symbol
                    self.compute()
                    self.state = self.State.SHOWING_RESULT

            elif symbol in binaryOperators:
                legit = True
                if self.firstOperand == '':
                    if symbol == 'r':
                        self.firstOperand = '2'
                    elif symbol == 'log':
                        self.firstOperand = '10'
                    elif symbol == '^':
                        self.firstOperand = 'e'
                    else:
                        legit = False
                if legit:
                    self.operator = symbol
                    self.state = self.State.TAKING_SECOND

            else:
                self.firstOperand = str(self.firstOperand) + str(symbol)

        elif self.state == self.State.TAKING_SECOND:
            if symbol == '=':
                if self.operator in binaryOperators and self.firstOperand == '':
                    if self.operator == 'log':
                        self.firstOperand = '10'
                    elif self.operator == 'r':
                        self.firstOperand = '2'
                self.compute()
                self.state = self.State.SHOWING_RESULT

            elif symbol == '-' and self.secondOperand == '':
                self.secondOperand = symbol

            elif symbol == 'C':
                self.clear()
                self.state = self.State.TAKING_FIRST

            elif symbol == 'CE':
                if not self.secondOperand == '':
                    self.secondOperand = self.secondOperand[:-1]

                elif not self.operator == '':
                    self.operator = ''
                    self.state = self.State.TAKING_FIRST

                elif not self.firstOperand == '':
                    self.firstOperand = self.firstOperand[:-1]
                    self.state = self.State.TAKING_FIRST

            elif symbol in unaryOperators:
                pass

            elif symbol in binaryOperators:
                pass

            else:
                self.secondOperand += str(symbol)

        elif self.state == self.State.SHOWING_RESULT:
            if symbol == '=':
                pass

            elif symbol == 'C':
                self.clear()
                self.state = self.State.TAKING_FIRST

            elif symbol == 'CE':
                if not self.firstOperand == '':
                    self.firstOperand = self.firstOperand[:-1]
                self.state = self.State.TAKING_FIRST

            elif symbol in unaryOperators:
                self.operator = symbol
                self.compute()

            elif symbol in binaryOperators:
                self.operator = symbol
                self.state = self.State.TAKING_SECOND

            else:
                self.firstOperand = str(symbol)
                self.state = self.State.TAKING_FIRST

        else:
            raise Exception('Illegal state')

        self.show()

    def compute(self):
        try:
            op0 = float(self.firstOperand)

            result = ''
            if self.operator in self.unaryMap.keys():
                fn = self.unaryMap[self.operator]
                result = fn(op0)

            elif self.operator in self.binaryMap.keys():
                op1 = float(self.secondOperand)
                fn = self.binaryMap[self.operator][0]
                if self.binaryMap[self.operator][1]:
                    result = fn(op1, op0)

                else:
                    result = fn(op0, op1)

            else:
                raise Exception('Unknown operator')

            result = round(result, 6)

            if float(result).is_integer():
                result = int(result)

            self.firstOperand = str(result)
            self.secondOperand = ''
            self.operator = ''

        except Exception:
            self.clear()
            self.firstOperand = 'Error'

    def show(self):
        printedOperator = self.operator

        if printedOperator in self.operatorMap.keys():
            printedOperator = self.operatorMap[printedOperator]

        if self.firstOperand in self.operandMap.keys():
            self.firstOperand = self.operandMap[self.firstOperand]

        if self.secondOperand in self.operandMap.keys():
            self.secondOperand = self.operandMap[self.secondOperand]

        self.printFn(f'{self.firstOperand} {printedOperator} {self.secondOperand}')


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
            self.pushButtonAbsolute,
            self.pushButtonSinus,
            self.pushButtonCosinus,
            self.pushButtonTangens,
            self.pushButtonClear,
            self.pushButtonClearEntry,
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
            (self.pushButtonDivide, '/'),
            (self.pushButtonMultiply, '*'),
            (self.pushButtonFactorial, '!'),
            (self.pushButtonAbsolute, 'a'),
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
