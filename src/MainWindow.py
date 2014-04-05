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


class MainWindow(QMainWindow, Ui_MainWindow):
    diag = 0
    Panel = 0
    prevCoM = QVector2D(0,0)
    currCoM = QVector2D(0,0)
    def __init__(self,MainPorgramm=None):
        QMainWindow.__init__(self)
        self.MainProgramm = MainPorgramm # Referenz zum Hauptprogramm speichern.
        self.setupUi(self)
        self.Panel = GraphPanel(self) # Erstellung der Grafikobjekte zum Anzeigen der Punkte
        self.Panel.setDragMode(QGraphicsView.RubberBandDrag)
        self.Panel.setGeometry(30,50,541,434)
        self.actionVerbinden.triggered.connect(self.MainProgramm.ConnectWiimotes) # Verbinden Menue bereitstellen
        self.actionBeenden.triggered.connect(self.close) # Butten zum schliessen des Programms
        
        
#Imoprt und Exportknöpfe
        self.rec.hide()
        self.play.hide()
        self.timeline.hide()
        self.playback_radio.setDisabled(True)
        self.live_radio.setDisabled(True)
             
# sind keine Punkte markiert, werden alle Optionen fuer verbindungen und den Referenzpunkt ausgeblende
        self.calibrate_button.setDisabled(True)
        self.connect_button.setDisabled(True)
        self.connect_button.pressed.connect(self.ConnectButtonPressed)
        self.ref_point_button.setEnabled(False)
        self.ref_point_button.pressed.connect(self.SelectRefPointButtonPressed)
    
    def PointSelected(self):
        #Diese Funktion wird aufgerufen wenn im Grafikpanel ein oder mehrere Punkte makiert wurden.
        #sind es 2 kann eine Verbindung erstellt oder geloescht werden. ist es einer gibt es eine
        #Option  zum Festlegen des Referenzpunktes
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
            if(len(self.Panel.scene.selectedItems()) == 1):
                self.ref_point_button.setEnabled(True)
            else:
                self.ref_point_button.setEnabled(False)
               

            
    def ConnectButtonPressed(self):
        if(self.connect_button.text() == "Punkte Verbinden"):
            self.MainProgramm.CreateJoint(self.Panel.scene.selectedItems())
        else:
            self.MainProgramm.DeleteJoint(self.Panel.scene.selectedItems())


    def SelectRefPointButtonPressed(self):
        self.MainProgramm.setReferencePoint(self.Panel.scene.selectedItems()[0])
        