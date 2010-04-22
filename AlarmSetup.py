
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

        self.createActions()
        self.createTrayIcon()
        self.trayIcon.setIcon(QtGui.QIcon('Resources/bell.png'))
        self.trayIcon.show()

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            QtGui.QMessageBox.information(self, "Systray",
                    "The program will keep running in the system tray. To "
                    "terminate the program, choose <b>Quit</b> in the "
                    "context menu of the system tray entry.")
            self.hide()
            event.ignore()

    def reject(self):
        self.close();
        print "reject()"

    def accept(self):
        print "Alarm1:",self.ui.lineEditAlarm1.text(),"Alarm2:",self.ui.lineEditAlarm2.text()
        self.close();
        self.timerLCD = AlarmTimer([int(self.ui.lineEditAlarm1.text()), int(self.ui.lineEditAlarm2.text())])
        self.timerLCD.show()
        self.timerLCD.Visible = True

    def createActions(self):
        self.toggleTimerAction = QtGui.QAction("&Toggle Timer", self,
                triggered=self.toggleTimer)

        self.settingsAction = QtGui.QAction("&Settings", self,
                triggered=self.showNormal)

        self.quitAction = QtGui.QAction("&Quit", self,
                triggered=QtGui.qApp.quit)

    def toggleTimer(self):
        if self.timerLCD.Visible:
            self.timerLCD.hide()
            self.timerLCD.Visible = False
        else:
            self.timerLCD.show()
            self.timerLCD.Visible = True


    def createTrayIcon(self):
         self.trayIconMenu = QtGui.QMenu(self)
         self.trayIconMenu.addAction(self.toggleTimerAction)
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