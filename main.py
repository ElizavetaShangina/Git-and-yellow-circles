from PyQt5 import uic
from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(600, 600)
        self.btn.clicked.connect(self.start_drawing)

    def start_drawing(self):
        self.btn.hide()
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor('yellow'))
        if self.btn.isHidden():
            self.btn.hide()
            for i in range(5000):
                self.drawing(qp)
            qp.end()

    def drawing(self, qp):
        a = randint(1, 100)
        x, y = randint(0, 500), randint(0, 500)
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main_Window()
    ex.show()
    exit(app.exec())

