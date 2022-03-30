from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtGui import QFont
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Animation Window")
        self.setGeometry(100, 100, 400, 400)
        self.widgets()
        self.show()

    def widgets(self):
        font = QFont("Times New Roman")
        font.setPixelSize(20)

        self.start = QPushButton("Start", self)
        self.start.setFont(font)
        self.start.setGeometry(100, 100, 100, 50)
        self.start.clicked.connect(self.doAnimation)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("background-color:darkGreen;")
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.setGeometry(250, 100, 100, 100)

    def doAnimation(self):
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(0, 0, 50, 100))
        self.anim.setEndValue(QRect(0, 0, 100, 500))
        self.anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())