import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("morze_ui.ui", self)

        self.lang = "ru"
        self.translate_btn.clicked.connect(self.run)
        self.btnTrans.clicked.connect(self.trans)

    def run(self):
        inp = self.textEdit.toPlainText()
        answer = to_morze(inp)
        self.answer_l.setText(answer)

    def trans(self):
        if self.lang == "ru":
            self.label.setText("Translation to the Morse. Enter the text:")
            self.translate_btn.setText("Translate")
            self.lang = "en"
        elif self.lang == "en":
            self.label.setText("Перевод в шифр морзе. Введите текст:")
            self.translate_btn.setText("Перевести")
            self.lang = "ru"
        else:
            self.label.setText("ERROR")


def to_morze(string):
    alphabet = {
        "А": "· −", "Б": "− · · ·", "В": "· − −", "Г": "− − ·", "Д": "− · ·", "Е": "·", "Ж": "· · · −", "З": "− − · ·",
        "И": "· ·", "Й": "· − − −", "К": "− · −", "Л": "· − · ·", "М": "− −", "Н": "− ·", "О": "− − −", "П": "· − − ·",
        "Р": "· − ·", "С": "· · ·", "Т": "−", "У": "· · −", "Ф": "· · − ·", "Х": "· · · ·", "Ц": "	− · − ·",
        "Ч": "	− − − ·", "Ш": "− − − −", "Щ": "− − · −", "Ъ": "− − · − −", "Ы": "− · − −", "Ь": "− · · −",
        "Э": "	· · − · ·", "Ю": "	· · − −", "Я": "· − · −", "1": "· − − − −", "2": "· · − − −", "3": "· · · − −",
        "4": "· · · · −", "5": "· · · · ·", "6": "	− · · · ·", "7": "− − · · ·", "8": "− − − · ·", "9": "− − − − ·",
        "0": "− − − − −", ".": "· · · · · ·", ",": "· − · − · −", ":": "− − − · · ·", "(": "	− · − − · −",
        '"': "	· − · · − ·", ";": "− · − · − ·", "'": "	· − − − − ·	", "-": "− · · · · −", "/": "− · · − ·",
        "?": "· · − − · ·", "!": "− − · · − −", "error": "· · · · · · · ·"
    }
    en_to_ru = {
        "A": "А", "B": "Б", "W": "В", "G": "Г", "D": "Д", "E": "Е", "V": "Ж", "Z": "З",
        "I": "И", "J": "Й", "K": "К", "L": "Л", "M": "М", "N": "Н", "O": "О", "P": "П",
        "R": "Р", "S": "С", "T": "Т", "U": "У", "F": "Ф", "H": "Х", "C": "Ц",
        "Q": "Щ", "Y": "Ы", "X": "Ь"
    }
    result = ""
    for symbol in string:
        symbol = symbol.upper()
        if symbol in en_to_ru.keys():
            symbol = en_to_ru[symbol]
        if symbol != " " and symbol != "\n":
            result += alphabet[symbol] + "  "
        else:
            result += "  "
    return result
