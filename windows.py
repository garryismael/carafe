from PyQt5.QtWidgets import (
    QWidget, QApplication, QFrame,
    QPushButton, QDesktopWidget,
    QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel
)
from PyQt5.QtCore import QPropertyAnimation, QRect, QTimer
from PyQt5.QtGui import QFont
import sys
from carafe import Carafe
from node import Noeud

from representation import Mesure


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.solution : list[Noeud] = []
        self.index = 0
        self.x_val = None
        self.y_val = None
        self.draw()

    def draw(self):
        self.center()
        self.form()
        self.galons()
        self.show()

    def form(self):
        self.groupbox_form = QGroupBox(self)
        self.v_box = QVBoxLayout()
        self.h_box_x = QHBoxLayout()
        self.h_box_y = QHBoxLayout()
        self.h_box_but = QHBoxLayout()
        self.create_button()

        self.label_x = QLabel('Galon 1:', self)
        self.label_y = QLabel('Galon 2:', self)
        self.label_but = QLabel('But:', self)
        self.line_x = QLineEdit(self)
        self.line_y = QLineEdit(self)
        self.line_but = QLineEdit(self)

        self.h_box_x.addWidget(self.label_x)
        self.h_box_x.addWidget(self.line_x)

        self.h_box_y.addWidget(self.label_y)
        self.h_box_y.addWidget(self.line_y)

        self.h_box_but.addWidget(self.label_but)
        self.h_box_but.addWidget(self.line_but)

        self.v_box.addLayout(self.h_box_x)
        self.v_box.addLayout(self.h_box_y)
        self.v_box.addLayout(self.h_box_but)

        self.v_box.addWidget(self.button)
        self.groupbox_form.setLayout(self.v_box)

    def create_button(self):
        font = QFont("Times New Roman")
        font.setPixelSize(20)
        self.button = QPushButton("Modifier", self)
        self.button.cursor()
        self.button.setFont(font)
        self.button.clicked.connect(self.changer_valeur)

    def galons(self):
        font = QFont("Times New Roman")
        font.setPixelSize(24)

        self.value_x = QLabel('x', self)
        self.value_y = QLabel('y', self)
        self.value_x.setFont(font)
        self.value_y.setFont(font)

        self.galon_x = QFrame(self)
        self.galon_x.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.galon_x.setGeometry(250, 10, 200, 250)
        self.value_x.move(340, 280)

        self.galon_y = QFrame(self)
        self.galon_y.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.galon_y.setGeometry(500, 10, 200, 250)
        self.value_y.move(590, 280)
        self.animate_galon()

    def animate_galon(self):
        self.g_x = QFrame(self)
        self.g_y = QFrame(self)

        self.g_x.setGeometry(250, 0, 200, 0)
        self.g_y.setGeometry(500, 0, 200, 0)

        self.g_x.setStyleSheet("background-color:#3366ff")
        self.g_y.setStyleSheet("background-color:#3366ff")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def changer_valeur(self):
        x = self.line_x.text()
        y = self.line_y.text()
        but = self.line_but.text()
        
        if x.isnumeric() and y.isnumeric() and but.isnumeric():
            x, y, but = int(x), int(y), int(but)
            self.x_val = x
            self.y_val = y
            carafe = Carafe(x, y, but)
            carafe.proceder()
            self.solution = carafe.solution
            for s in self.solution:
                print(s)
            print()
            self.button.setDisabled(True)
            self.mesure_x: Mesure = Mesure(0, 0, 0, 0)
            self.mesure_y: Mesure = Mesure(0, 0, 0, 0)
            self.index = 0
            self.timing()

    def timing(self):
        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.animate)
        self.timer.start()
            
    def animate(self):
        if self.index == len(self.solution):
            self.timer.stop()
            self.solution: list[Noeud] = []
            self.button.setDisabled(False)
            self.mesure_x = Mesure(0, 0, 0, 0)
            self.mesure_y = Mesure(0, 0, 0, 0)
            self.g_x.setGeometry(250, 0, 200, 0)
            self.g_y.setGeometry(500, 0, 200, 0)
            self.value_x.setText('x')
            self.value_y.setText('y')
            self.anim_x = QPropertyAnimation(self.g_x, b"geometry")
            self.anim_y = QPropertyAnimation(self.g_y, b"geometry")
            self.x_val = 0
            self.y_val = 0
        else:
            self.anim_x = QPropertyAnimation(self.g_x, b"geometry")
            self.anim_y = QPropertyAnimation(self.g_y, b"geometry")

            x = self.solution[self.index].x
            y = self.solution[self.index].y

            self.value_x.setText(str(x))
            self.value_y.setText(str(y))

            before_x_y = self.mesure_x.after_y
            before_x_h = self.mesure_x.after_h
            before_y_y = self.mesure_y.after_y
            before_y_h = self.mesure_y.after_h
            
            # VIDE
            if x == 0:
                self.mesure_x = Mesure(before_x_y, before_x_h, 0, 0)

            # VIDE
            if y == 0:
                self.mesure_y = Mesure(before_y_y, before_y_h, 0, 0)

            # PLEIN
            if x == self.x_val:
                self.mesure_x = Mesure(before_x_y, before_x_h, 10, 250)

            # PLEIN
            if y == self.y_val:
                self.mesure_y = Mesure(before_y_y, before_y_h, 10, 250)

            # MILIEU
            if x == self.x_val / 2:
                self.mesure_x = Mesure(before_x_y, before_x_h, 130, 130)

            if y == self.y_val / 2:
                self.mesure_y = Mesure(before_y_y, before_y_h, 130, 130)
            
            # A REVOIR
            # PRESQUE PLEIN
            if x > self.x_val / 2 and x < self.x_val:
                self.mesure_x = Mesure(before_x_y, before_x_h, 200, 190)

            if y > self.y_val / 2 and y < self.y_val:
                self.mesure_x = Mesure(before_y_y, before_y_h, 200, 190)
                
            # PRESQUE VIDE
            if x < self.x_val / 2 and x > 0:
                self.mesure_x = Mesure(before_x_y, before_x_h, 180, 80)
                
            if y > 0 and y < self.y_val / 2:
                self.mesure_y = Mesure(before_y_y, before_y_h, 180, 80)
                
            # set duration
            self.anim_x.setDuration(500)
            self.anim_y.setDuration(500)

            self.anim_x.setStartValue(
                QRect(250, self.mesure_x.before_y, 200, self.mesure_x.before_h)
            )
            self.anim_x.setEndValue(
                QRect(250, self.mesure_x.after_y, 200, self.mesure_x.after_h)
            )

            self.anim_y.setStartValue(
                QRect(500, self.mesure_y.before_y, 200, self.mesure_y.before_h)
            )
            self.anim_y.setEndValue(
                QRect(500, self.mesure_y.after_y, 200, self.mesure_y.after_h)
            )

            self.anim_x.start()
            self.anim_y.start()
            self.index += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
