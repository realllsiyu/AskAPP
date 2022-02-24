
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import *
from design import Ui_Form

import time
from key import key
from excel import excel
class Ask_App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.keyctl=key()
        self.keystatus=[0,0,0,0]
        

        self.current_choice=0

        self.current_question=1

        self.current_roll=1

        #questions and answers
        self.qusetion = ['What is your grade?', 'How are you feeling?']
        self.answer=[['9','10','11','12'],['red','yellow','blue','green']]

        #get the length of questions
        self.qusetion_num=len(self.qusetion)
        self.excel=excel('../excel/test.xls',self.qusetion)
        #connect to the UI file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #set the timer
        self.timer = QTimer(self)
        self.logictimer = QTimer(self)
        self.gpiotimer = QTimer(self)
        self.timer.timeout.connect(self.showtime)
        self.logictimer.timeout.connect(self.logic)
        self.gpiotimer.timeout.connect(self.key_read)
        self.timer.start(1000)
        self.logictimer.start(1000)
        self.gpiotimer.start(100)
        self.timeshow=self.get_time()

        self.qusetion_show()
        self.answer_show()
        self.info_show()
        #flags for the last or next question
        self.go_next_flag=0
    #go to the next question
    def go_next(self,if_save=True):
        self.go_next_flag=0
        if(if_save):
            self.excel.write_line(self.current_roll,self.current_question,self.answer[self.current_question-1][self.current_choice-1],self.timeshow)
            self.excel.last_save()

        if(self.current_question+1<=self.qusetion_num):
            self.current_question=self.current_question+1
            self.refresh_all()
        else:
            self.current_roll=self.current_roll+1
            self.current_question=1
            self.refresh_all()
        self.ui.b_red.setStyleSheet("QPushButton{background:#9E0000;color:white;border-radius: 30px;}")
        self.ui.b_yellow.setStyleSheet("QPushButton{background:#9E9E00;color:white;border-radius: 30px;}")
        self.ui.b_blue.setStyleSheet("QPushButton{background:#00009E;color:white;border-radius: 30px;}")
        self.ui.b_green.setStyleSheet("QPushButton{background:#009E00;color:white;border-radius: 30px;}")

    #返return to the last question
    def go_last(self):
        #still in the current round
        if self.current_question-1>0 :
            self.current_question=self.current_question-1
            self.refresh_all()
        #return to the last round
        elif self.current_roll-1>0:
            self.current_roll=self.current_roll-1
            self.current_question=self.qusetion_num
            self.refresh_all()
        else:
            self.refresh_all()
    #buttom events
    @QtCore.pyqtSlot()
    def on_b_red_clicked(self):
        self.ui.infolabel.setText('You chose：'+self.answer[self.current_question-1][0])
        self.current_choice=1
        self.go_next_flag=1
        self.ui.b_red.setStyleSheet("QPushButton{background:#FF0000;color:white;border-radius: 30px;}")
    @QtCore.pyqtSlot()
    def on_b_yellow_clicked(self):
        self.ui.infolabel.setText('You chose：'+self.answer[self.current_question-1][1])
        self.current_choice=2
        self.go_next_flag=1
        self.ui.b_yellow.setStyleSheet("QPushButton{background:#FFFF00;color:white;border-radius: 30px;}")

    @QtCore.pyqtSlot()
    def on_b_blue_clicked(self):
        self.ui.infolabel.setText('You chose：'+self.answer[self.current_question-1][2])
        self.current_choice=3
        self.go_next_flag=1
        self.ui.b_blue.setStyleSheet("QPushButton{background:#0000FF;color:white;border-radius: 30px;}")

    @QtCore.pyqtSlot()
    def on_b_green_clicked(self):
        self.ui.infolabel.setText('You chose：'+self.answer[self.current_question-1][3])
        self.current_choice=4
        self.go_next_flag=1
        self.ui.b_green.setStyleSheet("QPushButton{background:#00FF00;color:white;border-radius: 30px;}")

    @QtCore.pyqtSlot()
    def on_b_last_clicked(self):
        self.go_last()
    @QtCore.pyqtSlot()
    def on_b_next_clicked(self):
        #go into the next one without saving
        self.go_next(if_save=False)
    def key_read(self):
        keysta=self.keyctl.read()
        #when change occurs
        if(keysta!=self.keystatus):
            if(keysta[0]==0 ):
                self.on_b_red_clicked()
            elif(keysta[1]==0 ):
                self.on_b_yellow_clicked()
            elif(keysta[2]==0 ):
                self.on_b_blue_clicked()
            elif(keysta[3]==0 ):
                self.on_b_green_clicked()
            for i in range(4):
                self.keystatus[i]=keysta[i]
        
    def logic(self):
        if self.go_next_flag==1:
            time.sleep(1)
            self.go_next()
            

    #update time
    def showtime(self):
        self.timeshow=self.get_time()
        self.ui.timelabel.setText(self.timeshow)
    #update question
    def qusetion_show(self):
        self.ui.label.setText(self.qusetion[self.current_question-1])
    #update answer
    def answer_show(self):
        self.ui.b_red.setText(self.answer[self.current_question-1][0])
        self.ui.b_yellow.setText(self.answer[self.current_question-1][1])
        self.ui.b_blue.setText(self.answer[self.current_question-1][2])
        self.ui.b_green.setText(self.answer[self.current_question-1][3])
    #upodate instructions
    def info_show(self):
        self.ui.infolabel.setText("Current round number%d please answer%d " %(self.current_roll,self.current_question))

    #update UI
    def refresh_all(self):
        self.qusetion_show()
        self.answer_show()
        self.info_show()
    #get time from Internet
    def get_time(self):
        beijinTimeStr= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        return beijinTimeStr




