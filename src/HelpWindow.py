from PyQt5 import QtWidgets, uic

from os import path
import sys

bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
path_to_ui = path.abspath(path.join(bundle_dir, 'HelpWindow.ui'))


class UiHelpWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiHelpWindow, self).__init__()

        uic.loadUi(path_to_ui, self)

        self.show()
