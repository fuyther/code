<<<<<<< HEAD


from calc2 import MainWindow
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *


from PyQt5 import uic

=======
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLCDNumber
from math import sqrt
from PyQt5 import uic
from PyQt5 import QtGui
>>>>>>> 43e7f002f49d0123841779f1c0b2cc90360648ab
import sys
from morze import MyWidget
from weka2 import Example

<<<<<<< HEAD
=======
from calc2 import MainWindow


>>>>>>> 43e7f002f49d0123841779f1c0b2cc90360648ab
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.morze = MyWidget()
        self.cal = MainWindow()
        self.weka = Example()
        uic.loadUi("menu_ui1.ui", self)
        self.ruen_lan = "RU"
        col = QColor(255, 160, 122)
        col1 = QColor(0, 206, 209)
        col2 = QColor(152, 251, 50)
        col3 = QColor(255, 255, 240)
        self.centralwidget.setStyleSheet("QWidget { background-color: %s }" % col3.name())
        #self.btn_morze = QFrame(self)
        self.btn_morze.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.btn_system.setStyleSheet("QWidget { background-color: %s }" % col1.name())
        self.btn_calc.setStyleSheet("QWidget { background-color: %s }" % col2.name())
        #self.btn_morze.setStyleSheet('QPushButton:hover { color: red }')
        #self.btn_morze.resize(self.btn_morze.sizeHint())
        #self.btn_morze.setGeometry(0, 0, 100, 50)
        self.btn_morze.clicked.connect(self._morz)
        self.btn_system.clicked.connect(self.systm)
        self.ruen.clicked.connect(self.trans)
        self.btn_calc.clicked.connect(self.calc)

    def calc(self):
        if not self.cal:
            self.cal = MainWindow()
        self.cal.show()

    def trans(self):
        if self.ruen_lan == "RU":
            self.label.setText("Menu")
            self.btn_morze.setText("Morze")
            self.btn_calc.setText("Calculator")
            self.btn_system.setText("Number systems")
            self.ruen_lan = "EN"
        elif self.ruen_lan == "EN":
            self.label.setText("Меню")
            self.btn_morze.setText("Морзе")
            self.btn_calc.setText("Калькулятор")
            self.btn_system.setText("Системы исчисления")
            self.ruen_lan = "RU"
        else:
            self.label.setText("ERROR")

    def _morz(self):
        if not self.morze:
            self.morze = MyWidget()
        self.morze.show()

    def systm(self):
        if not self.weka:
            self.weka = Example()
        self.weka.show()


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())
