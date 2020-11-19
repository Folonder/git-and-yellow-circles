import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from random import choice


class Focus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Машинка')
        self.setMouseTracking(True)
        self.x = 0
        self.y = 0
        self.path = 'ufo.png'
        self.image = QLabel(self)
        pixmap = QPixmap(self.path)
        self.image.clear()
        self.image.move(self.x, self.y)
        self.image.resize(120, 70)
        self.image.setPixmap(pixmap)

    def keyPressEvent(self, event):
        pixmap = QPixmap(self.path)
        self.image.clear()
        if event.key() == Qt.Key_D:
            self.x += 15
            if self.x > 480:
                self.x = 0
        if event.key() == Qt.Key_S:
            self.y += 15
            if self.y > 530:
                self.y = 0
        if event.key() == Qt.Key_W:
            self.y -= 15
            if self.y < 0:
                self.y = 530
        if event.key() == Qt.Key_A:
            self.x -= 15
            if self.x < 0:
                self.x = 480
        self.image.move(self.x, self.y)
        self.image.resize(150, 100)
        self.image.setPixmap(pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())