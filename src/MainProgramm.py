# -*- coding: utf-8 -*-
'''
Created on 07.03.2014


Dieses Modul enthaelt die Hauptklasse, welche alle Elemente der Anwenung 
steuert.

@author: martin
'''

import MainWindow
from PyQt4.Qt import QTimer, QVector2D, QDialog, QMessageBox, QPointF,\
    QMainWindow

from Dialogs import MassRadDiag, ConnectDiag
from numpy import matrix, identity, linalg, zeros, reshape, vstack
import numpy
from copy import  copy
from ExportSave import SaveData, ExportCSV, LoadData
import cwiid

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
    
    #Trafos
    #Urbilder der Trafos
    BilderA = [None]*4
    BilderB = [None]*4   
    #PhysKS-> ViewKS

    Phys_View_KS = matrix([[200.0,0.0,500.0],[0.0,-200.0,500.0],[0.0,0.0,1.0]])
    #MoteKS-> PhysKS
    M_Phys_KS = [Phys_View_KS**-1,Phys_View_KS**-1]
    M_View_KS = [matrix(identity(3)),matrix(identity(3))]
    
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
                        Point =  HomPoint(data[i]['pos'][0]*1.0,data[i]['pos'][1]*1.0)
                        self.PointList[i+4*cnt] = Point
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
                # Trafo PhysKS -> View KS
                Point =   self.M_View_KS[i/4]*self.PointList[i]
                PointsToDraw.append(QPointF(Point.item(0),Point.item(1)))
                IDstoDraw.append(i)
            else:
                PointsToDraw.append(None)
                JointsToDraw = []
                for joint in self.JointList:
                    if set(IDstoDraw) >= joint[0]:
                        JointsToDraw.append(joint)            
        self.Window.Panel.redraw(PointsToDraw,[], self.DoPhysics())

 
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

        ExportCSV(self.RecordingTmpFile,'test1.csv')
        
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

    def SetKSTrafo(self, device_id):      
        
        unit =  [(0,0),(1,0),(0,1),(1,1)]
        bild = []
        if device_id == 0:
            for point in self.BilderA:
                bild.append((point.x(),point.y()))
        else:
            for point in self.BilderB:
                bild.append((point.x(),point.y()))
                        
        
        
        self.M_Phys_KS[device_id] = Homography( bild,unit)
        self.M_View_KS[device_id] = self.Phys_View_KS* self.M_Phys_KS[0]
        print self.M_Phys_KS[device_id]
    def AddCalPoint(self, Point, Type):
        ID = Point.ID()
        #Punkte in die Datenbank aufnehmen
        vector = self.PointList[ID]
        print vector
        if ID <4:
            self.BilderA[Type] = vector
            print self.BilderA.count(None) 
            if self.BilderA.count(None) == 0:
                self.Window.cal_state_A.setText('Kalibriert')
                print self.BilderA
                self.SetKSTrafo(0)
        else:
            self.BilderB[Type] = vector         
            if self.BilderB.count(None) == 0:
                self.Window.cal_state_B.setText('Kalibriert')
                self.SetKSTrafo(1)            

    def resetA(self):
        self.M_Phys_KS[0] = None
        self.M_View_KS[0] = identity(3)
        self.BilderA = [None]*4

    def resetB(self):
        self.M_Phys_KS[1] = None
        self.M_View_KS[1] = identity(3)   
        self.BilderB = [None]*4    
        
        

    
        
   
class HomPoint(matrix): 
    def __new__(self, x,y):
        return matrix.__new__(self,[[x],[y],[1]])

    def x(self):
        return self.item(0)/self.item(2)
    def y(self):
        return self.item(1)/self.item(2)   

def Homography( Urbilder,Bilder):        
    A = zeros((4*2,8))
    B = zeros((4*2,1))
    for i in range(0,4):
        A[2*i][0:2] = Urbilder[i]
        A[2*i][2] = 1
        A[2*i][6] = -Urbilder[i][0]*Bilder[i][0]
        A[2*i][7] = -Urbilder[i][1]*Bilder[i][0]
        A[2*i+1][3:5] = Urbilder[i]
        A[2*i+1][5] = 1
        A[2*i+1][6] = -Urbilder[i][0]*Bilder[i][1]
        A[2*i+1][7] = -Urbilder[i][1]*Bilder[i][1]
        B[2*i] = Bilder[i][0]
        B[2*i+1] = Bilder[i][1]

    X = linalg.lstsq(A,B)
    return reshape(vstack((X[0],[1])),(3,3))


class HomTransfrom(matrix):
    def __new__(self, *args, **kwargs):
        return matrix.__new__(self, *args, **kwargs)
    def __mul__(self, *args, **kwargs):
        erg = matrix.__mul__(self, *args, **kwargs)
        return matrix([erg.item(0)/erg.item(2),erg.item(1)/erg.item(2)]).T