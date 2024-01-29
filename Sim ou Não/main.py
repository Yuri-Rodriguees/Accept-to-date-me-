# -*- coding: utf-8 -*-

from PyQt5.QtCore import QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(QtWidgets.QMainWindow, object):
    def moveButton(self):
            self.frame_2.move(random.randint(0, 300), random.randint(0, 300))
            
    def eventFilter(self, obj, event):
            
            if event.type() == QEvent.Enter and obj == self.frame_2:
                    self.moveButton()
                    return True
            else:
                    return False
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 334)
        MainWindow.setMinimumSize(QtCore.QSize(424, 334))
        MainWindow.setMaximumSize(QtCore.QSize(424, 334))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/coracao.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(424, 334))
        self.centralwidget.setMaximumSize(QtCore.QSize(424, 334))
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(187, 210, 228, 255))\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 285, 27))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 190, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Button_sim = QtWidgets.QPushButton(self.frame)
        self.Button_sim.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.Button_sim.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(116, 116, 116);\n"
"border-style: solid;\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0, 255, 0);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(0, 255, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.Button_sim.setObjectName("Button_sim")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(260, 190, 120, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Button_nao = QtWidgets.QPushButton(self.frame_2)
        self.Button_nao.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.Button_nao.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(116, 116, 116);\n"
"border-style: solid;\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"}\n"
"")
        self.Button_nao.setObjectName("Button_nao")
        MainWindow.setCentralWidget(self.centralwidget)

        self.Button_nao.clicked.connect(self.moveButton)
        self.frame_2.installEventFilter(self)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sim ou Não?"))
        self.label.setText(_translate("MainWindow", "Você quer namorar comigo?"))
        self.Button_sim.setText(_translate("MainWindow", "SIM"))
        self.Button_nao.setText(_translate("MainWindow", "NÃO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
