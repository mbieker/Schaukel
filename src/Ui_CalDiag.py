# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal_diag.ui'
#
# Created: Sat May  3 21:24:48 2014
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

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(251, 145)
        DockWidget.setWindowOpacity(0.7)
        DockWidget.setFloating(True)
        DockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        DockWidget.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.dockWidgetContents)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 251, 118))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.output = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.output.setMouseTracking(True)
        self.output.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.output.setStatusTip(_fromUtf8(""))
        self.output.setAutoFillBackground(False)
        self.output.setStyleSheet(_fromUtf8("background-color:transparent\n"
""))
        self.output.setFrameShape(QtGui.QFrame.NoFrame)
        self.output.setLineWidth(0)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName(_fromUtf8("output"))
        self.verticalLayout_3.addWidget(self.output)
        self.button1 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button1.setFont(font)
        self.button1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button1.setStyleSheet(_fromUtf8(""))
        self.button1.setDefault(False)
        self.button1.setFlat(False)
        self.button1.setObjectName(_fromUtf8("button1"))
        self.verticalLayout_3.addWidget(self.button1)
        self.button2 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.button2.setObjectName(_fromUtf8("button2"))
        self.verticalLayout_3.addWidget(self.button2)
        self.button3 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.button3.setAutoFillBackground(True)
        self.button3.setObjectName(_fromUtf8("button3"))
        self.verticalLayout_3.addWidget(self.button3)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "DockWidget", None))
        self.output.setText(_translate("DockWidget", "TextLabel", None))
        self.button1.setText(_translate("DockWidget", "PushButton", None))
        self.button2.setText(_translate("DockWidget", "PushButton", None))
        self.button3.setText(_translate("DockWidget", "PushButton", None))

