from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

# Create the UnRar local environment variable.
from dotenv import load_dotenv
load_dotenv(override=True)

from unrar import rarfile


class UserInterface(QMainWindow):
	def __init__(self):
		super(UserInterface, self).__init__()
		uic.loadUi('.\\UI\\MainWindowUI.ui', self)
		self.show()


# Run program
app = QApplication(sys.argv)
program = UserInterface()
app.exec_()

