# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlarmSetupDialog.ui'
#
# Created: Sun Apr  4 20:18:36 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogAlarmSetup(object):
    def setupUi(self, DialogAlarmSetup):
        DialogAlarmSetup.setObjectName("DialogAlarmSetup")
        DialogAlarmSetup.resize(196, 141)
        DialogAlarmSetup.setMaximumSize(QtCore.QSize(234, 141))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/bell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAlarmSetup.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAlarmSetup)
        self.buttonBox.setGeometry(QtCore.QRect(20, 100, 164, 32))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.labelAlarm1 = QtGui.QLabel(DialogAlarmSetup)
        self.labelAlarm1.setGeometry(QtCore.QRect(20, 12, 89, 16))
        self.labelAlarm1.setObjectName("labelAlarm1")
        self.checkBoxRecurring = QtGui.QCheckBox(DialogAlarmSetup)
        self.checkBoxRecurring.setGeometry(QtCore.QRect(60, 70, 85, 20))
        self.checkBoxRecurring.setObjectName("checkBoxRecurring")
        self.lineEditAlarm1 = QtGui.QLineEdit(DialogAlarmSetup)
        self.lineEditAlarm1.setGeometry(QtCore.QRect(110, 8, 51, 23))
        self.lineEditAlarm1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditAlarm1.setObjectName("lineEditAlarm1")
        self.labelAlarm2 = QtGui.QLabel(DialogAlarmSetup)
        self.labelAlarm2.setGeometry(QtCore.QRect(20, 43, 89, 16))
        self.labelAlarm2.setObjectName("labelAlarm2")
        self.lineEditAlarm2 = QtGui.QLineEdit(DialogAlarmSetup)
        self.lineEditAlarm2.setGeometry(QtCore.QRect(110, 40, 51, 23))
        self.lineEditAlarm2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditAlarm2.setObjectName("lineEditAlarm2")

        self.retranslateUi(DialogAlarmSetup)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogAlarmSetup.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogAlarmSetup.reject)
        QtCore.QObject.connect(self.lineEditAlarm2, QtCore.SIGNAL("returnPressed()"), DialogAlarmSetup.accept)
        QtCore.QObject.connect(self.lineEditAlarm1, QtCore.SIGNAL("returnPressed()"), DialogAlarmSetup.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogAlarmSetup)
        DialogAlarmSetup.setTabOrder(self.lineEditAlarm1, self.lineEditAlarm2)
        DialogAlarmSetup.setTabOrder(self.lineEditAlarm2, self.buttonBox)

    def retranslateUi(self, DialogAlarmSetup):
        DialogAlarmSetup.setWindowTitle(QtGui.QApplication.translate("DialogAlarmSetup", "Alarm Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAlarm1.setText(QtGui.QApplication.translate("DialogAlarmSetup", "     Alarm 1     ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxRecurring.setText(QtGui.QApplication.translate("DialogAlarmSetup", "Recurring", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAlarm1.setToolTip(QtGui.QApplication.translate("DialogAlarmSetup", "minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAlarm1.setText(QtGui.QApplication.translate("DialogAlarmSetup", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAlarm2.setText(QtGui.QApplication.translate("DialogAlarmSetup", "     Alarm 2     ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAlarm2.setToolTip(QtGui.QApplication.translate("DialogAlarmSetup", "minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAlarm2.setText(QtGui.QApplication.translate("DialogAlarmSetup", "0", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
