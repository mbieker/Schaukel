# -*- coding: utf-8 -*-
'''
Created on 07.03.2014

Diese Klasse steuert das Verhalten des Hauptfensters
@author: martin
'''
from Ui_MainWindow import Ui_MainWindow
from PyQt4.QtGui import QMainWindow 
from PyQt4.Qt import QVector2D, QGraphicsView
from GraphicsPanel import GraphPanel
from Dialogs import ConnectDiag

class MainWindow(QMainWindow, Ui_MainWindow):
    diag = 0
    Panel = 0
    prevCoM = QVector2D(0,0)
    currCoM = QVector2D(0,0)
    def __init__(self,MainPorgramm=None):
        QMainWindow.__init__(self)
        self.MainProgramm = MainPorgramm
        self.setupUi(self)
        self.Panel = GraphPanel(self)
        self.Panel.setDragMode(QGraphicsView.RubberBandDrag)
        self.Panel.setGeometry(30,50,541,434)
        self.actionVerbinden.triggered.connect(self.MainProgramm.ConnectWiimotes)
        self.actionBeenden.triggered.connect(self.close)
        self.calibrate_button.setDisabled(True)
        self.connect_button.setDisabled(True)
        self.connect_button.pressed.connect(self.ConnectButtonPressed)
    
    def PointSelected(self):
        if len(self.Panel.scene.selectedItems()) == 2:
                PointSet = set([i.ID() for i in self.Panel.scene.selectedItems()])
                self.connect_button.setDisabled(False)
                self.calibrate_button.setDisabled(False)
                AllreadyConnected = False
                for joint in self.MainProgramm.JointList:
                    if(PointSet == joint[0]):
                        AllreadyConnected = True
                if AllreadyConnected:
                    self.connect_button.setText('Verbindung entferenen')
                else:
                    self.connect_button.setText("Punkte Verbinden")
                    
                
        else:
            self.calibrate_button.setDisabled(True)
            self.connect_button.setDisabled(True)  

            
    def ConnectButtonPressed(self):
        if(self.connect_button.text() == "Punkte Verbinden"):
            self.MainProgramm.CreateJoint(self.Panel.scene.selectedItems())
        else:
            self.MainProgramm.DeleteJoint(self.Panel.scene.selectedItems())


