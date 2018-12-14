from string import ascii_uppercase
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
import sys
from MainWindow import Ui_MainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        col = QColor(0, 206, 209)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(0, 0, 610, 600)

        uic.loadUi('weka.ui', self)
        self.btn.clicked.connect(self.hello)
        self.setWindowTitle('Перевод между системами исчисления')

    def hello(self):
        try:
            form = int(self.number_input.text())
            frm = self.name_input.text()
            to = int(self.number_input1.text())
            num = 0
            if (form in range(2, 36)) and (to in range(2, 36)):
                for i in range(len(frm)):
                    num += formation(frm[i]) * (form ** (len(frm) - (i + 1)))
                    if frm[i].upper() in ascii_uppercase:
                        if ascii_uppercase.index(frm[i].upper()) + 11 > form:
                            raise ValueError
                lst = []
                while num > 0:
                    lst.append(num - (num // to) * to)
                    num = num // to
                name = formation_(lst[::-1])
                self.buglabel.setFont(QtGui.QFont("Times", 10))
                self.buglabel.setText("Ответ: {}".format(name))
            elif form > 35 or to > 35:
                self.buglabel.setFont(QtGui.QFont("Times", 10))
                self.buglabel.setText("Заданная система исчисления больше 35")
            elif form < 2 or to < 2:
                self.buglabel.setFont(QtGui.QFont("Times", 10))
                self.buglabel.setText("Заданная система исчисления меньше 2")
        except ValueError:
            self.buglabel.setFont(QtGui.QFont("Times", 10))
            self.buglabel.setText("Error")


def formation(string):
    lst = ascii_uppercase
    if string.upper() in lst:
        string = lst.index(string.upper()) + 10
    else:
        string = int(string)
    return string


def formation_(lst):
    const = ascii_uppercase
    her = ""
    for i in range(len(lst)):
        if lst[i] > 9:
            her += const[lst[i] - 10]
        else:
            her += str(lst[i])
    return her
