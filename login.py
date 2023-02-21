from PyQt6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QPushButton, QRadioButton, QWidget, QApplication, QMessageBox
import sys
from PyQt6.QtCore import pyqtSignal, QObject

class Signal(QObject):
    signal = pyqtSignal()

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.signal = Signal()
        self.setWindowTitle("Login")
        self.setGeometry(500, 200, 250, 300)
        self.setFixedSize(250, 300)

        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("font-size: 14px; border-radius: 15px;")
        self.name_input.setPlaceholderText("Input your name")
        self.name_input.setFixedSize(200, 40)

        self.easy = QRadioButton("Easy")
        self.hard = QRadioButton("Hard")

        self.start = QPushButton("Start")
        self.start.setFixedSize(100, 40)
        self.start.clicked.connect(self.play)

        self.vertical = QVBoxLayout()
        self.vertical.addWidget(self.name_input)
        self.vertical.addWidget(self.easy)
        self.vertical.addWidget(self.hard)
        self.vertical.addWidget(self.start)

        center = QWidget(self)
        center.setLayout(self.vertical)
        self.setCentralWidget(center)

    def play(self):
        if self.name_input.text() == '':
            QMessageBox.critical(self, "Error", "Name field is empty")
        elif not (self.easy.isChecked() or self.hard.isChecked()):
            QMessageBox.critical(self, "Error", "Select mode empty")
        else:
            if self.easy.isChecked():
                mode = self.easy.text()
            elif self.hard.isChecked():
                mode = self.hard.text()
            name = self.name_input.text()
            self.signal.signal.emit(mode, name)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LoginPage()
    main.show()
    app.exec()
