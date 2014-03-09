'''
Created on 07.03.2014

@author: martin
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './massraddiag.ui'
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

class Ui_MassRadDialog(object):
    def setupUi(self, MassRadDialog):
        MassRadDialog.setObjectName(_fromUtf8("MassRadDialog"))
        MassRadDialog.setWindowModality(QtCore.Qt.WindowModal)
        MassRadDialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(MassRadDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(MassRadDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 351, 201))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 251, 141))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.mass = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.mass.setObjectName(_fromUtf8("mass"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.mass)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.umfang = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.umfang.setDecimals(4)
        self.umfang.setMaximum(1.0)
        self.umfang.setSingleStep(0.01)
        self.umfang.setObjectName(_fromUtf8("umfang"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.umfang)
        self.radius = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.radius.setPrefix(_fromUtf8(""))
        self.radius.setDecimals(4)
        self.radius.setMaximum(1.0)
        self.radius.setSingleStep(0.01)
        self.radius.setProperty("value", 0.0)
        self.radius.setObjectName(_fromUtf8("radius"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.radius)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)

        self.retranslateUi(MassRadDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MassRadDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MassRadDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MassRadDialog)

    def retranslateUi(self, MassRadDialog):
        MassRadDialog.setWindowTitle(_translate("MassRadDialog", "Verbindung erstellen", None))
        self.groupBox.setTitle(_translate("MassRadDialog", "Eigenschaften der Verbindung", None))
        self.label.setText(_translate("MassRadDialog", "Masse (kg)", None))
        self.label_2.setText(_translate("MassRadDialog", "Umfang (m)", None))
        self.label_3.setText(_translate("MassRadDialog", "Radius (m)", None))

