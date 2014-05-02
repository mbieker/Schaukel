# -*- coding: utf-8 -*-
'''
Created on 07.03.2014


Dieses Modul enthaelt die Hauptklasse, welche alle Elemente der Anwenung 
steuert.

@author: martin
'''

import MainWindow
from PyQt4.Qt import QTimer, QVector2D, QDialog, QMessageBox
import cwiid
import ExportSave
from Dialogs import MassRadDiag, ConnectDiag

from copy import  copy
from ExportSave import SaveData, ExportCSV, LoadData

class MainProgramm:
    
    PointList = [None]*8
    PointTimeOutList = [5]*8
    JointList = []
    #updateThread = []

    ReferencePoint = None
    TrackReferencePoint = None
    device_list = [None,None]
    renderTimer = None
    recording = False
    RecordingTmpFile = None
    DataSaved = True
    State = "S" # S-Stop/Pause , P-Play , L-Live(Record) 
    PlaybackPos = 0 

    def __init__(self ):
    

        self.Window = MainWindow.MainWindow(self)
        self.Window.show()
        self.renderTimer = QTimer()
        self.renderTimer.start(20)
        self.renderTimer.timeout.connect(self.Repaint)
        self.updateTimer = QTimer()
        self.updateTimer.timeout.connect(self.report)

                
    def report(self):
        cnt = 0
        for device in self.device_list:
          
            if not device == None:
                data = device.state['ir_src']
                for i in range(0,4):
                    if not data[i] == None:
                        #Position des Punktes updateten
                        self.PointList[i+4*cnt] = QVector2D(data[i]['pos'][0],data[i]['pos'][1])
                        self.PointTimeOutList[i+4*cnt] = 0
                    else:
                        #Punkt Connection Lost counter
                        if(self.PointTimeOutList[i+4*cnt] >= 5):
                            self.PointTimeOutList[i+4*cnt] = 5
                            self.PointList[i+4*cnt] = None
                        else:
                            self.PointTimeOutList[i+4*cnt] += 1
                cnt += 1
            
        if self.recording:
            self.RecordingTmpFile.append(copy(self.PointList))



    def CreateJoint(self,PointList):
        diag = MassRadDiag()
        if diag.exec_() == QDialog.Accepted:
            self.JointList.append((set([i.ID() for i in PointList]),diag.mass.value(), diag.radius.value()))
        self.Window.PointSelected()
        
    def DeleteJoint(self,PointList):
        PointsToRemove = set([i.ID() for i in PointList])
        for joint in self.JointList:
            if joint[0] == PointsToRemove:
                self.JointList.remove(joint)
                break
        self.Window.connect_button.setText("Punkte Verbinden")
        
    def DeleteAllJoints(self):
        self.JointList = []
        
    def ResetReferencePoint(self):
        self.ReferencePoint = None
        self.TrackReferencePoint = None
        
    def setReferencePoint(self, Point):
        oldRefPoint = self.ReferencePoint
        self.ReferencePoint = Point.ID()
        if not oldRefPoint == self.ReferencePoint:
            self.Window.Panel.setReferencePoint(self.ReferencePoint, oldRefPoint)
        else:
            self.ReferencePoint = None 
            self.Window.Panel.setReferencePoint(None, oldRefPoint)


    def Repaint(self):

        PointsToDraw = []
        IDstoDraw = []
        for i in range(8):
            if not self.PointList[i] == None:
                PointsToDraw.append(self.PointList[i].toPointF())
                IDstoDraw.append(i)
            else:
                PointsToDraw.append(None)
                JointsToDraw = []
                for joint in self.JointList:
                    if set(IDstoDraw) >= joint[0]:
                        JointsToDraw.append(joint)            
        self.Window.Panel.redraw(PointsToDraw,JointsToDraw, self.DoPhysics())

 
    def update_device_list(self):
        cnt = 0
        for i in self.device_list:
            if(isinstance(i, cwiid.Wiimote)):
                print 'Updates für Geraet ' + str(cnt) + 'gestartet'
                cnt += 1
            else:
                print 'Hier kein Gerät'
        if not cnt == 0:
            self.Window.live_radio.setEnabled(True)
            self.Window.live_radio.setChecked(True)
            self.Window.rec.show()

        else:
            self.Window.live_radio.setDisabled(True) 
            self.Window.hide()
                
                
    def DoPhysics(self):
        
        
        JointsToUse = []
        
        for joint in self.JointList:
            if  self.PointList[list(joint[0])[0]] != None and   self.PointList[list(joint[0])[1]] != None:
                JointsToUse.append(joint)      
        
        #Berechung des CoM
        CoM = QVector2D(0,0)
        TotalMass = 0
        for joint in JointsToUse:

            CoM += joint[1] * self.CenterOfJoint(joint)
            TotalMass += joint[1]
        
        CoM = CoM/TotalMass
        if TotalMass == 0:
            return None
        return CoM
        
        
        
        
    def CenterOfJoint(self, Joint):
        
        return 0.5*(self.PointList[list(Joint[0])[0]]+self.PointList[list(Joint[0])[1]])

    def ConnectWiimotes(self):
            diag = ConnectDiag(self.device_list)
            diag.exec_()
            self.update_device_list()
            
    def StartRecording(self):
        self.recording = True
        self.RecordingTmpFile = []
        return
    
    def StopRecording(self):
        self.recording = False
        self.DataSaved = False

        ExportSave.ExportCSV(self.RecordingTmpFile,'test1.csv')
        
    def Export(self, Filename):
        if not ExportCSV(self.RecordingTmpFile, Filename):
            QMessageBox(QMessageBox.Critical, "Fehler", "Speichern der Datei fehlgeschlagen", buttons = QMessageBox.Ok).exec_()

    
    def SaveFile(self, Filenmame):
        if not SaveData(self.RecordingTmpFile, self.JointList, self.ReferencePoint, Filenmame):
            QMessageBox(QMessageBox.Critical, "Fehler", "Speichern der Datei fehlgeschlagen", buttons = QMessageBox.Ok).exec_()
        else:
            self.DataSaved = True
       
    def LoadFile(self, Filename):
        data = LoadData(Filename)
        if data[0] :#Wurde allles korrekt gelesen?
            self.RecordingTmpFile ,self.JointList, self.ReferencePoint =  data[1]
            self.Window.playback_radio.setEnabled(True)
            self.Window.playback_radio.setChecked(True)

        else:
            QMessageBox(QMessageBox.Critical, "Fehler", "Laden der Datei fehlgeschlagen", buttons = QMessageBox.Ok).exec_()
            
    
    def LiveRadioToggled(self, checked):

        if checked:
            self.State = 'L'
            print "Hier auch"
            self.updateTimer.start(10)
        
            
        return 
    
    def PlaybackRadioToggled(self, checked):
        if checked:
            self.State = 'S'
            self.updateTimer.stop()
            self.PointList = self.RecordingTmpFile[0]
            self.PlaybackPos = 0
        return
        
        
        
    def PlayButtonToggled(self):
        self.State = "P"

        
    