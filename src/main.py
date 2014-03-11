# -*- coding: utf-8 -*-
'''
----Main Funktion----
Von hier wird das Hauptprogramm gestartet und die QApplication erzeugt
'''
from PyQt4.QtGui import QApplication
from sys import argv
import MainProgramm

app = QApplication(argv)

MainProgramm.MainProgramm()   

app.exec_()



