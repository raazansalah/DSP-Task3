from task3 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Functions (Ui_MainWindow):
    def __init__(self , window):
        self.setupUi(window)


app = QtWidgets.QApplication (sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Functions(MainWindow)

MainWindow.show()
app.exec_()