import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import randint


class Focus(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        return self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            self.x = randint(100, 500)
            self.y = randint(100, 500)
            radius = 20
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QBrush(QColor(255, 255, 0)))
            qp.drawEllipse(self.x - radius, self.y - radius, 2 * radius, 2 * radius)
            qp.end()
            self.do_paint = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())