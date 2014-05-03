'''
Created on 07.03.2014

@author: martin
'''

from PyQt4.Qt import QDialog
from numpy  import pi
from Ui_MassRadDiag import Ui_MassRadDialog
from Ui_ConnectDiag import *
from WiiMoteConnect import *

import Ui_CalDiag


class MassRadDiag(Ui_MassRadDialog,QDialog):
    def __init__(self, parent = None):
        Ui_MassRadDialog.__init__(self)
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.umfang.valueChanged.connect(self.conv_umfg_rad)
        self.radius.valueChanged.connect(self.conv_rad_umfg)
        self.buttonBox.setEnabled(False)
        self.mass.valueChanged.connect(self.checkMass)
    def conv_umfg_rad(self,Umfang):
        self.radius.setValue(Umfang/(2*pi))

    def conv_rad_umfg(self,Radius):
        self.umfang.setValue(Radius*2*pi)        

    def checkMass(self):
        if self.mass.value() != 0:
            self.buttonBox.setEnabled(True)
        else:
            self.buttonBox.setEnabled(False)
            
            
class ConnectDiag(QDialog, Ui_Dialog):
    
    thread = 0
    def __init__(self, device_list):
        QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)
        self.device_list = device_list
        if(self.device_list[0] == None):
            self.state_a.setText("Nicht Verbunden")
            self.state_a.setStyleSheet('background-color:rgb(255, 21, 21)')
        else:
            self.state_a.setText("Verbunden")
            self.state_a.setStyleSheet('background-color:rgb(0,255,0)')                      

        if(self.device_list[1] == None):
            self.state_b.setText("Nicht Verbunden")
            self.state_b.setStyleSheet('background-color:rgb(255, 21, 21)')
        else:
            self.state_b.setText("Verbunden")
            self.state_b.setStyleSheet('background-color:rgb(0,255,0)')          
        self.connect_a.clicked.connect(self.connectA)
        self.connect_b.clicked.connect(self.connectB)
        self.quit.clicked.connect(self.accept)       
    def connectA(self):
        print 'Button A pressed' 
        if( self.device_list[0] == None ):            
            self.thread =ConnectWiiMote(self.state_a, self.quit,self.device_list , 0)
            self.thread.start()
        else:

            self.state_a.setText('Nicht Verbunden')
            self.state_a.setStyleSheet('background-color:rgb(255, 21, 21)')
            self.device_list[0] = None
            

        
    def connectB(self):
        print 'Button B pressed' 
        if( self.device_list[1] == None ):            
            self.thread =ConnectWiiMote(self.state_b, self.quit,self.device_list , 1)
            self.thread.start()
        else:

            self.state_b.setText('Nicht Verbunden')
            self.state_b.setStyleSheet('background-color:rgb(255, 21, 21)')
            self.device_list[1] = None
            


class CalDiag(Ui_CalDiag.Ui_Dialog):
    def __init__(self, parent):

        Ui_CalDiag.Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.parent = parent

              
    