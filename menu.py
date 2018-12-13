import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from morze import MyWidget
from weka2 import Example


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.morze = MyWidget()
        self.weka = Example()
        uic.loadUi("menu_ui.ui", self)
        self.btn_morze.clicked.connect(self._morz)
        self.btn_system.clicked.connect(self.systm)

    def _morz(self):
        if not self.morze:
            self.morze = MyWidget()
        self.morze.show()

    def systm(self):
        if not self.weka:
            self.weka = Example()
        self.weka.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
