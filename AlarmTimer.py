import sys
from PyQt4 import QtCore, QtGui
from itertools import cycle

from Resources.LcdNumber_ui import Ui_Form


class AlarmTimer(QtGui.QMainWindow):
    def __init__(self, timer_values, parent=None):
        QtGui.QWidget.__init__(self, parent)
        QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Initialize member variables
        self.color_names = [ "Normal", "Yellow" ]
        self.color_idx = 1
        self.updateTimers(timer_values)
        self.cur_timer = self.timer_iter.next()      # Current timer value
        self.snooze_time = 1 * 60
        self.show()
        self.oneSecondCounter = 0
        #self.showTimer()

        # Start a timer for 1s(=1000ms) and call showTimer() every second
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTimer)
        timer.start(250)
        

    def showTimer(self):
        text = "%d:%02d" % (self.cur_timer/60,self.cur_timer % 60)
        self.ui.lcdNumber.display(text)
        if (self.cur_timer == 0):
            self.color_idx = 3 - self.color_idx
            self.show()
            self.setStyleSheet("QWidget { background-color: %s }" % self.color_names[self.color_idx - 1])
        elif self.oneSecondCounter == 3:
            self.cur_timer -= 1
            self.oneSecondCounter = 0
        else:
            self.oneSecondCounter += 1

    def updateTimers(self, timer_list):
        self.alarm_times = timer_list
        self.timer_iter = cycle(self.alarm_times)    # An iterator that cycles through the list

    def mouseReleaseEvent(self, event):
        button = event.button()
        if button == 2:
            self.hide()
            if (self.cur_timer == 0):
                self.cur_timer = self.snooze_time        # Start the timer with snooze value if teh cur_timer has expired
        elif button == 1: # left click
            if (self.cur_timer == 0): # blinking timer should be closed on a left click
                self.cur_timer = self.timer_iter.next()
                self.setStyleSheet("QWidget { background-color: Normal }" )

    def mousePressEvent(self, event):
        button = event.button()
        if button == 1:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft();

    def mouseMoveEvent(self, event):
        if event.buttons() != QtCore.Qt.LeftButton: # not left click
            return 
        
        self.move(event.globalPos() - self.dragPosition)


def Str2Num(str_list):
    num = []
    for str in str_list:
        try:
            num.append(int(str))
        except ValueError:
            num.append(float(str))
    return num

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    timerList = Str2Num(sys.argv[1:])
    myapp = AlarmTimer(timerList)
    myapp.show()
    sys.exit(app.exec_())

