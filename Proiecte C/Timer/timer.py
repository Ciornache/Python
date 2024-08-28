from PySide6.QtWidgets import QApplication, QDialog, QLineEdit
import PySide6.QtTest as QtTest
import sys 
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class Timer(QtCore.QObject):

    def __init__(self):

        super().__init__()
        self.ui = loader.load('Ui-Elements/timer.ui')
        self.ui.setWindowTitle('My Timer')
        self.ui.show()
        self.ui.startButton.pressed.connect(self.startButtonPressed)
        self.ui.stopButton.pressed.connect(self.stopButtonPressed)
        self.ui.lineEdit_2.textChanged.connect(self.registerText)
        self.ui.lineEdit_4.textChanged.connect(self.registerText)
        self.ui.lineEdit.editingFinished.connect(self.editingFinished)
        self.ui.lineEdit_2.editingFinished.connect(self.editingFinished)
        self.ui.lineEdit_4.editingFinished.connect(self.editingFinished)
        self.noHoverStyleSheet = """ QLineEdit {
                        border:0px 0px 0px 0px;
                        font-size: 25px;
                        background-color:transparent;
                        min-width:40px;
                        max-width:40px;
                        min-height:55px;
                        max-height:55px;
                        border-radius:15%;
                    }"""

    def startButtonPressed(self):
        
        hours = self.ui.lineEdit.displayText()
        minutes = self.ui.lineEdit_4.displayText()
        seconds = self.ui.lineEdit_2.displayText()

        if not hours or not minutes or not seconds:
            return None

        self.ui.lineEdit.setStyleSheet(self.noHoverStyleSheet)
        self.ui.lineEdit_2.setStyleSheet(self.noHoverStyleSheet)
        self.ui.lineEdit_4.setStyleSheet(self.noHoverStyleSheet)

        time = [hours, minutes, seconds]
        self.stop = False
        time = time[::-1]

        while not self.stop:
            ok = False
            for index, element in enumerate(time):
                if not ok and element != '00':
                    if element[1] != '0':
                        time[index] = time[index][0] + str(int(element[1]) - 1)
                    else:
                        time[index] = str(int(element[0]) - 1) + '9'
                    ok = True
                    for index2 in range(0, index):
                        time[index2] = '59'
            
            self.ui.lineEdit_2.setText(time[0])
            self.ui.lineEdit_4.setText(time[1])
            self.ui.lineEdit.setText(time[2])
            self.stop = not ok

            QtTest.QTest.qWait(1000)


    def stopButtonPressed(self):
        self.stop = True
    
    def registerText(self):
        sender = self.sender()
        time = sender.displayText()

        for ch in time:
            if not str.isdigit(ch):
                sender.setText(time[:len(time)-1])
                return None 

        if len(time) > 0 and int(time[0]) > 0 and int(time) >= 60:
            sender.setText(time[0])
        
    def editingFinished(self):
        sender = self.sender()
        time = sender.displayText()
        if len(time) != 2:
            sender.setText('0' + time)

    
app = QApplication(sys.argv)
timer = Timer()
app.exec()
