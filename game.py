from PyQt5 import QtCore, QtGui, QtWidgets
from style import Style
from check import Check_win
from main import Computer_second


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 420)
        MainWindow.setMinimumSize(QtCore.QSize(510, 420))
        MainWindow.setMaximumSize(QtCore.QSize(510, 420))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.Page = QtWidgets.QTabWidget(self.centralwidget)
        self.Page.setMinimumSize(QtCore.QSize(350, 350))
        self.Page.setMaximumSize(QtCore.QSize(350, 350))
        self.Page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Page.setStyleSheet("")
        self.Page.setObjectName("Page")

        self.game_page = QtWidgets.QWidget()
        self.game_page.setStyleSheet("")
        self.game_page.setObjectName("game_page")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.game_page)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.btn_1 = QtWidgets.QPushButton(self.game_page)
        self.btn_1.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_1.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        
        self.gridLayout_2.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_2 = QtWidgets.QPushButton(self.game_page)
        self.btn_2.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_2.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_2.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_3 = QtWidgets.QPushButton(self.game_page)
        self.btn_3.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_3.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_2.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_4 = QtWidgets.QPushButton(self.game_page)
        self.btn_4.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_4.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_2.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_5 = QtWidgets.QPushButton(self.game_page)
        self.btn_5.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_5.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_2.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_6 = QtWidgets.QPushButton(self.game_page)
        self.btn_6.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_6.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_2.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_7 = QtWidgets.QPushButton(self.game_page)
        self.btn_7.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_7.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 2, 0, 1, 1)

        self.btn_8 = QtWidgets.QPushButton(self.game_page)
        self.btn_8.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_8.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 2, 1, 1, 1)

        self.btn_9 = QtWidgets.QPushButton(self.game_page)
        self.btn_9.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_9.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 2, 2, 1, 1)

        self.Page.addTab(self.game_page, "")

        self.about_page = QtWidgets.QWidget()
        self.about_page.setObjectName("about_page")
        self.Page.addTab(self.about_page, "")
        self.gridLayout.addWidget(self.Page, 0, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.start_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self.start)

        self.horizontalLayout.addWidget(self.start_btn)

        self.about_btn = QtWidgets.QPushButton(self.centralwidget)
        self.about_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.about_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.about_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_btn.setObjectName("about_btn")
        self.horizontalLayout.addWidget(self.about_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.Score = QtWidgets.QLabel("Score:\nPlayer1: 0\nPlayer2: 0\nDraw: 0")
        self.Score.setStyleSheet("font-size: 14px;")
        self.verticalLayout.addWidget(self.Score)


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 100))
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_list = [
            [self.btn_1, self.btn_2, self.btn_3],
            [self.btn_4, self.btn_5, self.btn_6],
            [self.btn_7, self.btn_8, self.btn_9]
        ]
        self.btn_1.clicked.connect(lambda: self.move(0, 0))
        self.btn_2.clicked.connect(lambda: self.move(0, 1))
        self.btn_3.clicked.connect(lambda: self.move(0, 2))
        self.btn_4.clicked.connect(lambda: self.move(1, 0))
        self.btn_5.clicked.connect(lambda: self.move(1, 1))
        self.btn_6.clicked.connect(lambda: self.move(1, 2))
        self.btn_7.clicked.connect(lambda: self.move(2, 0))
        self.btn_8.clicked.connect(lambda: self.move(2, 1))
        self.btn_9.clicked.connect(lambda: self.move(2, 2))
        self.restart()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Page.setTabText(self.Page.indexOf(self.game_page), _translate("MainWindow", "Play"))
        self.Page.setTabText(self.Page.indexOf(self.about_page), _translate("MainWindow", "About"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.about_btn.setText(_translate("MainWindow", "About"))
        self.label_2.setText(_translate("MainWindow", "Player 1"))
        self.label_3.setText(_translate("MainWindow", "Player 2"))


    def restart(self):
        Style.TURN == -1
        self.label_2.setStyleSheet(Style.normal())
        self.label_3.setStyleSheet(Style.normal())
        for btns in self.btn_list:
            for btn in btns:
                btn.setEnabled(False)
                btn.setText(' ')
        

    def start(self):
        Style.TURN = 0
        self.label_2.setStyleSheet(Style.active())
        self.label_3.setStyleSheet(Style.inactive())
        for btns in self.btn_list:
            for btn in btns:
                btn.setText(' ')
                btn.setEnabled(True)


    def move(self, row: int, col: int):
        if Style.TURN == 0:
            self.btn_list[row][col].setText("X")
            self.btn_list[row][col].setStyleSheet(Style.X())
            self.label_3.setStyleSheet(Style.active())
            self.label_2.setStyleSheet(Style.inactive())
            self.btn_list[row][col].setEnabled(False)
            Style.TURN = 1
            if self.check() == 1:
                return
            self.comp_move()


    def comp_move(self):
        # btn = Computer_second.easy(self.btn_list)
        btn = Computer_second.hard(Computer_second, self.btn_list)
        btn.setText("O")
        btn.setStyleSheet(Style.O())
        self.label_2.setStyleSheet(Style.active())
        self.label_3.setStyleSheet(Style.inactive())
        btn.setEnabled(False)
        Style.TURN = 0
        self.check()

    def check(self):
        winner = Check_win.winner(self.btn_list)
        if winner == 1:
                self.message = QtWidgets.QMessageBox.about(self, "Winner", f"{self.label_2.text()} win!")
                self.restart()
                Check_win.PLAYER1 += 1
                self.Score.setText(f"Score:\nPlayer1: {Check_win.PLAYER1}\nPlayer2: {Check_win.PLAYER2}\nDraw: {Check_win.DRAW}")
                return 1
        if winner == 2:
                self.message = QtWidgets.QMessageBox.about(self, "Winner", f"{self.label_3.text()} win!")
                self.restart()
                Check_win.PLAYER2 += 1
                self.Score.setText(f"Score:\nPlayer1: {Check_win.PLAYER1}\nPlayer2: {Check_win.PLAYER2}\nDraw: {Check_win.DRAW}")
                return 1
        if winner == 0:
            if Check_win.is_all_occupied(self.btn_list):
                self.message = QtWidgets.QMessageBox.about(self, "Winner", "Draw")
                self.restart()
                Check_win.DRAW += 1
                self.Score.setText(f"Score:\nPlayer1: {Check_win.PLAYER1}\nPlayer2: {Check_win.PLAYER2}\nDraw: {Check_win.DRAW}")
                return 1


