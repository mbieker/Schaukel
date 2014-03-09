'''
Created on 07.03.2014

@author: martin
'''
from PyQt4.Qt import pyqtSignal, QThread
import cwiid
import time 
class UpdateWiiMote(QThread):
    pos_update = pyqtSignal(list,int)
    def __init__(self, WiiMote_id, caller ):
        QThread.__init__(self)
        
        self.caller = caller # Referenz zum Aufrufer
        self.device_list = caller.device_list #device_list des MainProgramms laden
        self.WiiMote_id = WiiMote_id #Referenz zur WiiMote lokal speichren
        self.device_list[self.WiiMote_id].rpt_mode = cwiid.RPT_IR
   
        
    def run(self):
        self.pos_update.connect(self.caller.report)  
        while True:
            
            if(not self.device_list[self.WiiMote_id] == None):
                self.pos_update.emit( self.device_list[self.WiiMote_id].state['ir_src'],self.WiiMote_id)

            
class ConnectWiiMote(QThread):

    state_box_text = pyqtSignal(str)
    state_box_color = pyqtSignal(str) 
    def __init__(self, state_box, quit_box , device_list, id):
        QThread.__init__(self)
        self.id = id
        self.device_list = device_list
        self.state_box_text.connect(state_box.setText)
        self.state_box_color.connect(state_box.setStyleSheet)

    def run(self):
        self.state_box_text.emit("Verbinden...")
        self.state_box_color.emit("background-color:rgb(255,255,0)")
        time.sleep(2)
        try:
            self.device_list[self.id] = cwiid.Wiimote()
            self.device_list[self.id].led = 12
            self.state_box_text.emit("Verbunden")
            self.state_box_color.emit('background-color:rgb(0,255,0)')
        except RuntimeError:
            print "Error"
            self.state_box_text.emit("Error")
            self.state_box_color.emit('background-color:rgb(255, 21, 21)')
            
        
