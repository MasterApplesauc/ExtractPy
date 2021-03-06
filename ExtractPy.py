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
		self.connectUI()

	def connectUI(self):
		''' Connect UI elements pythonically '''
		self.btn_Extract.clicked.connect(lambda: print('Extract Clicked'))
		self.btn_Clear.clicked.connect(lambda: print('Clears the file list'))
		self.btn_Settings.clicked.connect(lambda: print('Opens the settings menu'))


# Run program
app = QApplication(sys.argv)
program = UserInterface()
app.exec_()

