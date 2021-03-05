from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys

class UserInterface(QMainWindow):
	def __init__(self):
		super(UserInterface, self).__init__()
		uic.loadUi('.\\UI\\MainWindowUI.ui', self)
		self.show()


# Run program
app = QApplication(sys.argv)
program = UserInterface()
app.exec_()

