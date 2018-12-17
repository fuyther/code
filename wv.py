import wave
import sys
import struct
import pygame

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *


from PyQt5 import uic


class WV(QMainWindow):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.songisgoing = False
        self.newdata = []
        self.mixer = pygame.mixer
        self.song = self.mixer.Sound
        uic.loadUi("wv_ui1.ui", self)
        try:
            self.open.setShortcut('Ctrl + 0')
            self.open.triggered.connect(self.open_f)
            self.save_as.triggered.connect(self.save_asf)
            self.play.clicked.connect(self.play_)
            self.pause.clicked.connect(self.pause_)
            self.stop.clicked.connect(self.stop_)
            self.volume_slider.valueChanged.connect(self.volum)
        except Exception:
            QMessageBox.critical(self, "DON'T DO THIS!", "CERTAINLY, DONT'T TOUCH ANYTHING")

    def play_(self):
        if not self.songisgoing:
            op = wave.open("wv_op/variable.wav", "wb")
            op.setparams(self.file.getparams())
            op.writeframes(self.newframes)
            self.song = self.mixer.Sound(op)
            clock = pygame.time.Clock()
            self.time.setText(clock)
            self.song.play()
            self.songisgoing = True
            while True:
                clock.tick(24)
            self.songisgoing = False
            pygame.quit()
        else:
            pygame.mixer.unpause()

    def volum(self):
        value = self.volume_slider.value()
        self.newdata = volume(self.newdata, value / 100)
        self.newframes = struct.pack("<" + str(len(self.newdata)) + "h", *self.newdata)
        self.mixer.music.set_volume(value / 100)

    def pause_(self):
        self.song.pause()

    def stop_(self):
        self.song.stop()

    def reverse_(self):
        self.newdata = reverse(self.newdata)

    def speed_(self, mult):
        self.newdata = speed(self.newdata, mult)

    def add_(self):
        path = QFileDialog.getOpenFileName(self, 'Open file', filter="*.wav")
        file = wave.open(path[0], "rb")
        frames_num = file.getnframes()
        frames = file.readframes(frames_num)
        data = struct.unpack("<" + str(frames_num) + "h", frames)
        self.newdata = add_(self.newdata, data)

    def open_f(self):
        path = str(QFileDialog.getOpenFileName(self, 'Open file', filter="*.wav")[0])
        self.file = wave.open(path, "rb")
        self.frames_num = self.file.getnframes()
        self.frames = self.file.readframes(self.frames_num)
        self.newframes = self.frames
        self.data = struct.unpack("<" + str(self.frames_num) + "h", self.frames)
        self.newdata = self.data
        self.total_time.setText(self.frames_num//24)

    def save_asf(self):
        path = QFileDialog.getSaveFileName(self, 'Save file as', filter="*.wav")[0]
        file = wave.open(path, "wb")
        file.setparams(self.file.getparams())
        self.newframes = struct.pack("<" + str(len(self.newdata)) + "h", *self.newdata)
        file.writeframes(self.newframes)


def reverse(data):
    return data[::-1]


def volume(data, multiple):
    return list(map(lambda x: x * multiple, data))


def speed(data, multiple):
    res = []
    for index, frame in enumerate(data):
        if multiple >= 1 and multiple.is_digit():
            for i in range(multiple):
                res.append(frame)
        elif multiple >= 1:
            res.append(frame)
            if index % (1 / multiple) == 0:
                res.append(frame)
        else:
            if index % (1 / multiple) == 0:
                res.append(frame)
    return res


def add_(data1, data2):
    if data1 > data2:
        data_res = data1[:]
        for frame in data2:
            data_res.append(frame)
    else:
        data_res = data2[:]
        for frame in data1:
            data_res.append(frame)
    return data_res


app = QApplication(sys.argv)
ex = WV()
ex.show()
sys.exit(app.exec_())
