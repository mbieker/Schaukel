# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat May  3 13:58:22 2014
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
        self.groupBox_2.setGeometry(QtCore.QRect(600, 160, 181, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.connect_button = QtGui.QPushButton(self.groupBox_2)
        self.connect_button.setGeometry(QtCore.QRect(10, 40, 171, 27))
        self.connect_button.setObjectName(_fromUtf8("connect_button"))
        self.ref_point_button = QtGui.QPushButton(self.groupBox_2)
        self.ref_point_button.setGeometry(QtCore.QRect(10, 80, 171, 27))
        self.ref_point_button.setObjectName(_fromUtf8("ref_point_button"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(600, 40, 181, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 161, 42))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cal_state_A = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.cal_state_A.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.cal_state_A.setObjectName(_fromUtf8("cal_state_A"))
        self.verticalLayout_4.addWidget(self.cal_state_A)
        self.cal_state_B = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.cal_state_B.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 4);"))
        self.cal_state_B.setObjectName(_fromUtf8("cal_state_B"))
        self.verticalLayout_4.addWidget(self.cal_state_B)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(610, 290, 171, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.rec = QtGui.QPushButton(self.groupBox_3)
        self.rec.setGeometry(QtCore.QRect(10, 60, 98, 27))
        self.rec.setObjectName(_fromUtf8("rec"))
        self.timeline = QtGui.QSlider(self.groupBox_3)
        self.timeline.setGeometry(QtCore.QRect(10, 100, 160, 19))
        self.timeline.setOrientation(QtCore.Qt.Horizontal)
        self.timeline.setObjectName(_fromUtf8("timeline"))
        self.live_radio = QtGui.QRadioButton(self.centralwidget)
        self.live_radio.setGeometry(QtCore.QRect(620, 430, 114, 22))
        self.live_radio.setObjectName(_fromUtf8("live_radio"))
        self.playback_radio = QtGui.QRadioButton(self.centralwidget)
        self.playback_radio.setGeometry(QtCore.QRect(620, 450, 114, 22))
        self.playback_radio.setObjectName(_fromUtf8("playback_radio"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuWiiMotes = QtGui.QMenu(self.menubar)
        self.menuWiiMotes.setObjectName(_fromUtf8("menuWiiMotes"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        self.menuMessung = QtGui.QMenu(self.menubar)
        self.menuMessung.setObjectName(_fromUtf8("menuMessung"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVerbinden = QtGui.QAction(MainWindow)
        self.actionVerbinden.setObjectName(_fromUtf8("actionVerbinden"))
        self.actionBeenden = QtGui.QAction(MainWindow)
        self.actionBeenden.setObjectName(_fromUtf8("actionBeenden"))
        self.new_project = QtGui.QAction(MainWindow)
        self.new_project.setObjectName(_fromUtf8("new_project"))
        self.load_project = QtGui.QAction(MainWindow)
        self.load_project.setObjectName(_fromUtf8("load_project"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionSpeichern = QtGui.QAction(MainWindow)
        self.actionSpeichern.setObjectName(_fromUtf8("actionSpeichern"))
        self.actionLaden = QtGui.QAction(MainWindow)
        self.actionLaden.setObjectName(_fromUtf8("actionLaden"))
        self.actionCal = QtGui.QAction(MainWindow)
        self.actionCal.setObjectName(_fromUtf8("actionCal"))
        self.menuWiiMotes.addAction(self.actionVerbinden)
        self.menuWiiMotes.addSeparator()
        self.menuWiiMotes.addAction(self.actionBeenden)
        self.menuInfo.addAction(self.actionCal)
        self.menuInfo.addAction(self.actionAbout)
        self.menuMessung.addAction(self.actionExport)
        self.menuMessung.addAction(self.actionSpeichern)
        self.menuMessung.addAction(self.actionLaden)
        self.menubar.addAction(self.menuWiiMotes.menuAction())
        self.menubar.addAction(self.menuMessung.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Konfiguration", None))
        self.connect_button.setText(_translate("MainWindow", "Punkte Verbinden", None))
        self.ref_point_button.setText(_translate("MainWindow", "Referenzpunkt setzen", None))
        self.groupBox.setTitle(_translate("MainWindow", "Eichung", None))
        self.cal_state_A.setText(_translate("MainWindow", "WM A nicht kalibriert", None))
        self.cal_state_B.setText(_translate("MainWindow", "WM B nicht kalibriert", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Messung", None))
        self.rec.setText(_translate("MainWindow", "Aufnehmen", None))
        self.live_radio.setText(_translate("MainWindow", "Live Ansicht", None))
        self.playback_radio.setText(_translate("MainWindow", "Widergabe", None))
        self.menuWiiMotes.setTitle(_translate("MainWindow", "Datei", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Einstellungen", None))
        self.menuMessung.setTitle(_translate("MainWindow", "Messung", None))
        self.actionVerbinden.setText(_translate("MainWindow", "WiiMotes Verbinden", None))
        self.actionVerbinden.setShortcut(_translate("MainWindow", "C", None))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden", None))
        self.actionBeenden.setShortcut(_translate("MainWindow", "Q", None))
        self.new_project.setText(_translate("MainWindow", "Neue Messung", None))
        self.load_project.setText(_translate("MainWindow", "Messung Laden", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionExport.setText(_translate("MainWindow", "Als CSV exportieren", None))
        self.actionSpeichern.setText(_translate("MainWindow", "Speichern", None))
        self.actionLaden.setText(_translate("MainWindow", "Laden", None))
        self.actionCal.setText(_translate("MainWindow", "Kalibrieren", None))

