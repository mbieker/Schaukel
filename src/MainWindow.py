# -*- coding: utf-8 -*-
'''
Created on 07.03.2014

Diese Klasse steuert das Verhalten des Hauptfensters
@author: martin
'''
from Ui_MainWindow import Ui_MainWindow
from PyQt4.QtGui import QMainWindow 
from PyQt4.Qt import QVector2D, QGraphicsView, QMessageBox, QFileDialog
from GraphicsPanel import GraphPanel
from MainProgramm import *


class MainWindow(QMainWindow, Ui_MainWindow):
    diag = 0
    Panel = 0
    prevCoM = QVector2D(0,0)
    currCoM = QVector2D(0,0)
    def __init__(self,MainProgramm=None):
        QMainWindow.__init__(self)
        self.MainProgramm = MainProgramm # Referenz zum Hauptprogramm speichern.
        self.setupUi(self)
        self.Panel = GraphPanel(self) # Erstellung der Grafikobjekte zum Anzeigen der Punkte
        self.Panel.setDragMode(QGraphicsView.RubberBandDrag)
        self.Panel.setGeometry(30,50,541,434)
        
# Verbinden Menue bereitstellen 

        #Datei
        self.actionVerbinden.triggered.connect(self.MainProgramm.ConnectWiimotes) 
        self.actionBeenden.triggered.connect(self.close) # Butten zum schliessen des Programms
        #Messung 
        self.actionSpeichern.triggered.connect(self.SaveAction)
        self.actionLaden.triggered.connect(self.LoadAction)
        self.actionExport.triggered.connect(self.ExportAction)
        
        
        #Imoprt und Exportknöpfe
        self.rec.hide()
        self.timeline.hide()
        self.playback_radio.setDisabled(True)
        self.live_radio.setDisabled(True)
        self.playback_radio.toggled.connect(self.MainProgramm.PlaybackRadioToggled)
        self.live_radio.toggled.connect(self.MainProgramm.LiveRadioToggled)
        self.rec.clicked.connect(self.RecButtonToggled)   
                 
# sind keine Punkte markiert, werden alle Optionen fuer verbindungen und den Referenzpunkt ausgeblende

        self.connect_button.setDisabled(True)
        self.connect_button.pressed.connect(self.ConnectButtonPressed)
        self.ref_point_button.setEnabled(False)
        self.ref_point_button.pressed.connect(self.SelectRefPointButtonPressed)
        self.cal_O.setDisabled(True)
        self.cal_O.pressed.connect(self.CalOToggeld)
        self.cal_X.setDisabled(True)
        self.cal_X.pressed.connect(self.CalXToggeld)
        self.cal_Y.setDisabled(True)
        self.cal_Y.pressed.connect(self.CalYToggeld)   
    def PointSelected(self):
        #Diese Funktion wird aufgerufen wenn im Grafikpanel ein oder mehrere Punkte makiert wurden.
        #sind es 2 kann eine Verbindung erstellt oder geloescht werden. ist es einer gibt es eine
        #Option  zum Festlegen des Referenzpunktes
        if len(self.Panel.scene.selectedItems()) == 2:
                PointSet = set([i.ID() for i in self.Panel.scene.selectedItems()])
                self.connect_button.setDisabled(False)

                AllreadyConnected = False
                for joint in self.MainProgramm.JointList:
                    if(PointSet == joint[0]):
                        AllreadyConnected = True
                if AllreadyConnected:
                    self.connect_button.setText('Verbindung entferenen')
                else:
                    self.connect_button.setText("Punkte Verbinden")
                    
                
        else:

            self.connect_button.setDisabled(True)  
            if(len(self.Panel.scene.selectedItems()) == 1):
                self.ref_point_button.setEnabled(True)
                self.cal_O.setEnabled(True)
                self.cal_X.setEnabled(True)
                self.cal_Y.setEnabled(True)
            else:
                self.ref_point_button.setEnabled(False)
                self.cal_O.setEnabled(False)
                self.cal_X.setEnabled(False)
                self.cal_Y.setEnabled(False)               

            
    def ConnectButtonPressed(self):
        if(self.connect_button.text() == "Punkte Verbinden"):
            self.MainProgramm.CreateJoint(self.Panel.scene.selectedItems())
        else:
            self.MainProgramm.DeleteJoint(self.Panel.scene.selectedItems())


    def SelectRefPointButtonPressed(self):
        self.MainProgramm.setReferencePoint(self.Panel.scene.selectedItems()[0])
        
    def RecButtonToggled(self):
        if self.rec.text() == 'Aufnehmen':
            if not self.MainProgramm.DataSaved :
                msgbox = QMessageBox(QMessageBox.Question, "Frage", "Soll die vorherige Messung ueberschrieben werden ?", QMessageBox.No| QMessageBox.Yes)
                if not msgbox.exec_() == QMessageBox.Yes:
                    return
            self.MainProgramm.StartRecording()
            self.Panel.setRecFrame(True)
            self.rec.setText('Stop')
            
            
        else:
            self.MainProgramm.StopRecording()
            self.rec.setText("Aufnehmen")
            self.Panel.setRecFrame(False)
            self.playback_radio.setEnabled(True)
            
            
    def SaveAction(self):
        #Filename zum Speichern vom Benutzer erfragen
        filename = QFileDialog.getSaveFileName(self, 'Messung Speichern')
        if not filename == '':
            self.MainProgramm.SaveFile(filename)
        
        
    def LoadAction(self):
        if not self.MainProgramm.DataSaved :
            msgbox = QMessageBox(QMessageBox.Question, "Frage", "Soll die vorherige Messung ueberschrieben werden ?", QMessageBox.No| QMessageBox.Yes)
            if not msgbox.exec_() == QMessageBox.Yes:
                return
        filename = QFileDialog.getOpenFileName(self,"Messung laden")
        if not filename == '':
            self.MainProgramm.LoadFile(filename)
        return
        
        
    
    def ExportAction(self):
        filename = QFileDialog.getSaveFileName(self, 'Messung Exportieren')
        if not filename == '':
            self.MainProgramm.Export(filename)
        return
    
    def CalOToggeld(self):
        self.MainProgramm.AddCalPoint(self.Panel.scene.selectedItems()[0],0)     
        return

    def CalXToggeld(self):
        self.MainProgramm.AddCalPoint(self.Panel.scene.selectedItems()[0],1)    
    
    def CalYToggeld(self):
        self.MainProgramm.AddCalPoint(self.Panel.scene.selectedItems()[0],2)    