# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './connect_diag.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(358, 239)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 311, 151))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.connect_a = QtGui.QPushButton(self.verticalLayoutWidget)
        self.connect_a.setObjectName(_fromUtf8("connect_a"))
        self.gridLayout.addWidget(self.connect_a, 0, 2, 1, 1)
        self.connect_b = QtGui.QPushButton(self.verticalLayoutWidget)
        self.connect_b.setObjectName(_fromUtf8("connect_b"))
        self.gridLayout.addWidget(self.connect_b, 1, 2, 1, 1)
        self.state_b = QtGui.QLabel(self.verticalLayoutWidget)
        self.state_b.setStyleSheet(_fromUtf8("background-color:rgb(255, 21, 21);"))
        self.state_b.setFrameShape(QtGui.QFrame.Box)
        self.state_b.setObjectName(_fromUtf8("state_b"))
        self.gridLayout.addWidget(self.state_b, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.state_a = QtGui.QLabel(self.verticalLayoutWidget)
        self.state_a.setStyleSheet(_fromUtf8("background-color:rgb(255, 21, 21);"))
        self.state_a.setFrameShape(QtGui.QFrame.Box)
        self.state_a.setObjectName(_fromUtf8("state_a"))
        self.gridLayout.addWidget(self.state_a, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.quit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.quit.setObjectName(_fromUtf8("quit"))
        self.horizontalLayout.addWidget(self.quit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Zum Verbinden der WiiMotes auf dem jeweiligen Gerät\n"
"die Buttons 1 und 2 drücken und auf Verbinden klicken", None))
        self.connect_a.setText(_translate("Dialog", "Verbinden", None))
        self.connect_b.setText(_translate("Dialog", "Verbinden", None))
        self.state_b.setText(_translate("Dialog", "Dummy", None))
        self.label_3.setText(_translate("Dialog", "WiiMote A", None))
        self.label_2.setText(_translate("Dialog", "WiiMote B", None))
        self.state_a.setText(_translate("Dialog", "Dummy", None))
        self.quit.setText(_translate("Dialog", "Fertig", None))

