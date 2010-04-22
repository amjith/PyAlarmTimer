
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

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTimer)
        timer.start(500)
        
        self.color_names = [ "Normal", "Black" ]
        self.color_idx = 1
        self.alarm_times = timer_values
        self.timer_iter = cycle(self.alarm_times)
        self.sleep_time = self.timer_iter.next()
        self.timer_expired = False
        self.snooze_time = 5
        self.showTimer()

    def showTimer(self):
        text = "%d:%02d" % (0,self.sleep_time)
        self.ui.lcdNumber.display(text)
        if (self.sleep_time == 0):
            self.color_idx = 3 - self.color_idx
            self.show()
            self.Visible = True
            self.setStyleSheet("QWidget { background-color: %s }" % self.color_names[self.color_idx - 1])
            self.timer_expired = True
        else:
            self.sleep_time -= 1

    def mouseReleaseEvent(self, event):
        button = event.button()
        if button == 2:
            self.hide()
            self.Visible = False
        elif button == 1: # left click
            if (self.timer_expired): # blinking timer should be closed on a left click
                self.sleep_time = self.timer_iter.next()
                self.timer_expired = False
                self.setStyleSheet("QWidget { background-color: Normal }" )

    def mousePressEvent(self, event):
        button = event.button()
        if button == 1:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft();
        elif button == 2:
            print "Right Click"

    def mouseMoveEvent(self, event):
        button = event.button()
        if event.buttons() != QtCore.Qt.LeftButton: # not left click
            return 
        
        self.move(event.globalPos() - self.dragPosition)

#    def runAlarm( time_list ):
#        minute = 5     # one minute = 5 seconds
#
#        while (1):
#            for t in time_list:
#                cur_time = t 
#                print cur_time
#                while ( cur_time > 0 ):
#                    time.sleep(minute)
#                    cur_time -= 1
#                    print cur_time
#                   
#                print "Alarm:",t
#                sys.stdout.flush();
#                doit = raw_input("Continue (Y/N)?[Y]: ")
#                if doit == 'N' or doit=='n':
#                    print "Exiting....."
#                    return

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
