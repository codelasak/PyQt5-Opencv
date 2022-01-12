from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(700,300,500,500)
        self.setWindowTitle("Bismillah PyQt5")
        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Vira Bislimllah GUI World")
        self.label.move(250,250)

        self.b1 =QtWidgets.QPushButton(self)
        self.b1.setText("Dont Click Me")
        self.b1.move(50,250)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("oh man")
        self.update()

    def update(self):
        self.label.adjustSize()
        
    


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
