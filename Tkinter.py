import sys
import math
from builtins import StopIteration
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QFrame, QComboBox, QPushButton, QLineEdit, \
    QInputDialog, QTabWidget, QFileDialog, QColorDialog, QCheckBox, QListView, QDialog
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QPixmap, QCursor, QImage, QIcon

from PyQt5.QtCore import Qt, QPoint, QTimer, QEvent, QSize, QTimerEvent
from time import sleep, time
from random import randint


class GameLife(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.setGeometry(400, 400, 400, 400)
        self.n = 1
        self.lbl = QLabel(self)
        self.lbl.move(100, 100)
        self.lbl.resize(100, 100)
        self.lbl.setText(str(self.n))
        self.timer.timeout.connect(self.w)
        self.timer.start(500)

    def timerEvent(self, event):
        if event.TimerId() == self.timer.TimerId():
            print(1)

    def w(self):
        self.lbl.setText(str(self.n))
        self.n += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mand = GameLife()
    mand.show()
    sys.exit(app.exec())
