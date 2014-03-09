# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_window.ui'
#
# Created: Fri Mar  7 17:57:46 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(843, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(600, 160, 171, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.connect_button = QtGui.QPushButton(self.groupBox_2)
        self.connect_button.setGeometry(QtCore.QRect(10, 40, 161, 27))
        self.connect_button.setObjectName(_fromUtf8("connect_button"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(600, 40, 171, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 160, 80))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scale_label = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.scale_label.setObjectName(_fromUtf8("scale_label"))
        self.verticalLayout_4.addWidget(self.scale_label)
        self.calibrate_button = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.calibrate_button.setObjectName(_fromUtf8("calibrate_button"))
        self.verticalLayout_4.addWidget(self.calibrate_button)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(600, 270, 161, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuWiiMotes = QtGui.QMenu(self.menubar)
        self.menuWiiMotes.setObjectName(_fromUtf8("menuWiiMotes"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        self.menuDaten = QtGui.QMenu(self.menubar)
        self.menuDaten.setObjectName(_fromUtf8("menuDaten"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVerbinden = QtGui.QAction(MainWindow)
        self.actionVerbinden.setObjectName(_fromUtf8("actionVerbinden"))
        self.actionBeenden = QtGui.QAction(MainWindow)
        self.actionBeenden.setObjectName(_fromUtf8("actionBeenden"))
        self.menuWiiMotes.addAction(self.actionVerbinden)
        self.menuWiiMotes.addSeparator()
        self.menuWiiMotes.addAction(self.actionBeenden)
        self.menubar.addAction(self.menuWiiMotes.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menubar.addAction(self.menuDaten.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Konfiguration", None))
        self.connect_button.setText(_translate("MainWindow", "Punkte Verbinden", None))
        self.groupBox.setTitle(_translate("MainWindow", "Eichung", None))
        self.scale_label.setText(_translate("MainWindow", "Massstab: ?? px/m", None))
        self.calibrate_button.setText(_translate("MainWindow", "Kalibieren", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Messung", None))
        self.menuWiiMotes.setTitle(_translate("MainWindow", "Datei", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.menuDaten.setTitle(_translate("MainWindow", "Daten", None))
        self.actionVerbinden.setText(_translate("MainWindow", "WiiMotes Verbinden", None))
        self.actionVerbinden.setShortcut(_translate("MainWindow", "C", None))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden", None))
        self.actionBeenden.setShortcut(_translate("MainWindow", "Q", None))

