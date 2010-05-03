
import sys
from PyQt4 import QtCore, QtGui

#from AlarmSetupDialog_ui import Ui_DialogAlarmSetup
from Resources.AlarmSetupDialog_ui import Ui_DialogAlarmSetup
from AlarmTimer import AlarmTimer

class AlarmSetup(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_DialogAlarmSetup()
        self.ui.setupUi(self)
        intValidator = QtGui.QIntValidator(0,999,self.ui.lineEditAlarm1) # create a int validator with range from 0 to 999
        self.ui.lineEditAlarm1.setValidator(intValidator);
        self.ui.lineEditAlarm2.setValidator(intValidator);

        # System Tray
        self.createActions()
        self.createTrayIcon()
        self.trayIcon.setIcon(QtGui.QIcon(':Icons/bell.png'))
        self.trayIcon.show()
        self.trayMsgDisplayed = False
    
        self.trayIcon.activated.connect(self.iconActivated)

        # Lcd Timer display
        self.initializeTimers = True

    def closeEvent(self, event):
        if self.trayIcon.isVisible() and self.trayMsgDisplayed == False:
            QtGui.QMessageBox.information(self, "Systray",
                    "The program will keep running in the system tray. To "
                    "terminate the program, choose <b>Quit</b> in the "
                    "context menu of the system tray entry.")
            self.hide()
            event.ignore()
            self.trayMsgDisplayed = True

    def reject(self):
        self.close();

    def accept(self):
        #print "Alarm1:",self.ui.lineEditAlarm1.text(),"Alarm2:",self.ui.lineEditAlarm2.text(), "Recurring:", self.ui.checkBoxRecurring.value()
        timer_list = [int(self.ui.lineEditAlarm1.text()) * 60, int(self.ui.lineEditAlarm2.text()) * 60 ]
        if self.initializeTimers:
            self.timerLCD = AlarmTimer(timer_list) # Create a new timer with zero minutes
            self.initializeTimers = False
        else:
            self.timerLCD.updateTimers(timer_list) # Convert minutes to seconds
        self.close();

    def createActions(self):
        self.toggleTimerAction = QtGui.QAction("&Toggle Timer", self,
                triggered=self.toggleTimer)

        self.pauseTimerAction = QtGui.QAction("&Pause/Play Timer", self,
                triggered=self.pauseTimer)
        
        self.resetTimerAction = QtGui.QAction("&Reset Timer", self,
                triggered=self.resetTimer)

        self.settingsAction = QtGui.QAction("&Settings", self,
                triggered=self.showNormal)

        self.quitAction = QtGui.QAction("&Quit", self,
                triggered=QtGui.qApp.quit)


    def iconActivated(self, reason):
        if reason in (QtGui.QSystemTrayIcon.Trigger, QtGui.QSystemTrayIcon.DoubleClick):
            self.toggleTimer()

    def pauseTimer(self):
        self.timerLCD.pauseTimer()

    def resetTimer(self):
        self.timerLCD.resetTimer()
        

    def toggleTimer(self):
        try:
            if self.timerLCD.isVisible():
                self.timerLCD.hide()
            else:
                self.timerLCD.show()
        except AttributeError:
            return

    def createTrayIcon(self):
         self.trayIconMenu = QtGui.QMenu(self)
         self.trayIconMenu.addAction(self.toggleTimerAction)
         self.trayIconMenu.addAction(self.pauseTimerAction)
         self.trayIconMenu.addAction(self.resetTimerAction)
         self.trayIconMenu.addSeparator()
         self.trayIconMenu.addAction(self.settingsAction)
         self.trayIconMenu.addSeparator()
         self.trayIconMenu.addAction(self.quitAction)

         self.trayIcon = QtGui.QSystemTrayIcon(self)
         self.trayIcon.setContextMenu(self.trayIconMenu)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        QtGui.QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)

    QtGui.QApplication.setQuitOnLastWindowClosed(False)

    myapp = AlarmSetup()
    myapp.show()
    sys.exit(app.exec_())
