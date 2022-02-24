
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_Form(object):
    def setupUi(self, Form):
        #set the window's size
        self.width=1200
        self.height=600
        #set the virtual buttom size
        self.buttonsize=210
        #set the font size
        self.buttonfont=40
        self.infolabelfont=25
        self.timelabelfont=25
        self.labelfont=41

        font = QtGui.QFont()
        Form.setObjectName("问答系统")
        Form.resize(self.width, self.height)
        Form.setWindowFlags(Qt.FramelessWindowHint)
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.black)
        Form.setPalette(palette)
        # Form.setAttribute(Qt.WA_TranslucentBackground)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, self.width-20, self.height-90))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.infolabel = QtWidgets.QLabel(Form)
        self.infolabel.move(250, 25)
        self.infolabel.setFixedSize(500, 35)
        font.setPointSize(self.infolabelfont)
        self.infolabel.setFont(font)
        self.infolabel.setStyleSheet("QLabel{\n"
                                     "color:white};")
        
        self.timelabel = QtWidgets.QLabel(Form)
        self.timelabel.setFixedSize(500, 35)
        self.timelabel.move(self.width-500, 25)
        font.setPointSize(self.timelabelfont)
        self.timelabel.setFont(font)
        self.timelabel.setStyleSheet("QLabel{\n"
                                     "color:white};")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(600, 0))
        font.setPointSize(self.labelfont)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
                                     "color:white};")

        #last question buttom
        self.b_last = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_last.setMinimumSize(QtCore.QSize(40, 250))
        self.b_last.setMaximumSize(QtCore.QSize(50, 16777215))
        self.b_last.setObjectName("b_last")
        self.b_last.setStyleSheet("QPushButton{\n"
                                   "border-image: url(../res/left.jpg);\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "border-image: url(../res/left_press.jpg);\n"
                                    "}"
                                    )
        self.horizontalLayout.addWidget(self.b_last, 0, QtCore.Qt.AlignLeft)

        #next question buttom
        self.horizontalLayout.addWidget(self.label)
        self.b_next = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_next.setMinimumSize(QtCore.QSize(40, 250))
        self.b_next.setMaximumSize(QtCore.QSize(50, 16777215))
        self.b_next.setObjectName("b_next")
        self.b_next.setStyleSheet("QPushButton{\n"
                                   "border-image: url(../res/right.jpg);\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "border-image: url(../res/right_press.jpg);\n"
                                    "}"
                                    )
        self.horizontalLayout.addWidget(self.b_next, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #red
        self.b_red = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_red.setMinimumSize(QtCore.QSize(80, 80))
        self.b_red.setMaximumSize(QtCore.QSize(self.buttonsize, self.buttonsize))
        self.b_red.setObjectName("b_red")
        font.setPointSize(self.buttonfont)
        self.b_red.setFont(font)
        self.b_red.setStyleSheet("QPushButton{\n"
                                    "    background:#9E0000;\n"
                                    "    color:white;\n"
                                    "    border-radius: 30px;\n"
                                    "}\n")
        self.horizontalLayout_2.addWidget(self.b_red)
        #yellow
        self.b_yellow = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_yellow.setMinimumSize(QtCore.QSize(80, 80))
        self.b_yellow.setMaximumSize(QtCore.QSize(self.buttonsize, self.buttonsize))
        self.b_yellow.setObjectName("b_yellow")
        font.setPointSize(self.buttonfont)
        self.b_yellow.setFont(font)
        self.b_yellow.setStyleSheet("QPushButton{\n"
                                    "    background:#9E9E00;\n"
                                    "    color:white;\n"
                                    "    border-radius: 30px;\n"
                                    "}\n")

        self.horizontalLayout_2.addWidget(self.b_yellow)

        self.b_blue = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_blue.setMinimumSize(QtCore.QSize(80, 80))
        self.b_blue.setMaximumSize(QtCore.QSize(self.buttonsize, self.buttonsize))
        self.b_blue.setObjectName("b_blue")
        font.setPointSize(self.buttonfont)
        self.b_blue.setFont(font)
        self.b_blue.setStyleSheet("QPushButton{\n"
                                    "    background:#00009E;\n"
                                    "    color:white;\n"
                                    "    border-radius: 30px;\n"
                                    "}\n")
        self.horizontalLayout_2.addWidget(self.b_blue)
        #green
        self.b_green = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_green.setMinimumSize(QtCore.QSize(80, 80))
        self.b_green.setMaximumSize(QtCore.QSize(self.buttonsize, self.buttonsize))
        self.b_green.setObjectName("b_green")
        font.setPointSize(self.buttonfont)
        self.b_green.setFont(font)
        self.b_green.setStyleSheet("QPushButton{\n"
                                    "    background:#009E00;\n"
                                    "    color:white;\n"
                                    "    border-radius: 30px;\n"
                                    "}\n")
        #blue
        self.horizontalLayout_2.addWidget(self.b_green)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget.raise_()
        self.b_red.raise_()

        #close
        self.button_red = QPushButton(Form)
        self.button_red.move(20, 20)
        self.button_red.setFixedSize(40, 40)
        self.button_red.setStyleSheet("QPushButton{\n"
                                         "    background:#CE0000;\n"
                                         "    color:white;\n"
                                         "    border-radius: 20px;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:red!important;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    border: 1px solid #3C3C3C!important;\n"
                                         "    background:black;\n"
                                         "}")
        self.button_red.clicked.connect(self.quit_button)
 
        self.button_orange = QPushButton(Form)
        self.button_orange.move(70, 20)
        self.button_orange.setFixedSize(40, 40)
        self.button_orange.setStyleSheet("QPushButton{\n"
                                 "    background:orange;\n"
                                 "    color:white;\n"
                                 "    border-radius: 20px;\n"
                                 "}\n"
                                 "QPushButton:hover{                    \n"
                                 "    background:yellow!important;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "    border: 1px solid #3C3C3C!important;\n"
                                 "    background:black;\n"
                                 "}")
 
        self.button_green = QPushButton(Form)
        self.button_green.move(120, 20)
        self.button_green.setFixedSize(40, 40)
        self.button_green.setStyleSheet("QPushButton{\n"
                                    "    background:green;\n"
                                    "    color:white;\n"
                                    "    border-radius: 20px;\n"
                                    "}\n"
                                    "QPushButton:hover{                    \n"
                                    "    background:#08BF14!important;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    border: 1px solid #3C3C3C!important;\n"
                                    "    background:black;\n"
                                    "}")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def quit_button(self):
        quit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "问答系统"))
        self.label.setText(_translate("Form", "问题框"))


