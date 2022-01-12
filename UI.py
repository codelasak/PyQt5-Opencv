from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(700,300,500,500)
    win.setWindowTitle("Bismillah PyQt5")

    label = QtWidgets.QLabel(win)
    label.setText("Vira Bislimllah GUI World")
    # label.move(250,250)

    win.show()
    sys.exit(app.exec_())


window()
