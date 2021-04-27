"""!@file HelpWindow.py
@brief Contains class used to open tutorial window.
"""

from PyQt5 import QtWidgets, uic

from os import path
import sys

# Path to a directory containing project
bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
# Path to a ui file created in QT Creator
path_to_ui = path.abspath(path.join(bundle_dir, 'HelpWindow.ui'))


class UiHelpWindow(QtWidgets.QMainWindow):
    """!Class used for creation of a new window.
    """

    def __init__(self):
        """!Inilization of ui from file created in QT Creator.
        """
        super(UiHelpWindow, self).__init__()

        uic.loadUi(path_to_ui, self)

        self.show()
