from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randrange
import sys


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.can_draw = False
        self.draw.clicked.connect(self.draw_el)
        self.setWindowTitle('Рисование желтых кругов')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.yellow,  8, Qt.SolidLine))
        diam = randrange(1, 500)
        painter.drawEllipse(0, 0, diam, diam)

    def draw_el(self):
        self.can_draw = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())