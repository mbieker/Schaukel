from PyQt4.QtCore import *
from PyQt4.QtGui import *


  
class Point(QGraphicsEllipseItem):
    
    colorlist = [Qt.red,Qt.green,Qt.yellow, Qt.blue, Qt.lightGray, Qt.black, Qt.cyan, Qt.magenta]
    point_id = 0
    
    def __init__(self,parent,scene,PointId):
        self.wasSelected = False
        QGraphicsEllipseItem.__init__(self,scene=scene)
        self.setRect(-10,-10,20,20)
        self.setBrush(QBrush(self.colorlist[PointId]))
        self.point_id = PointId
        self.moveBy(20,20)
        self.hide()
        self.isseclected= False
        self.parent = parent
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def itemChange(self, *args, **kwargs):
        if(args[0]== 14):
            self.parent.parent.PointSelected()

        return QGraphicsEllipseItem.itemChange(self, *args, **kwargs)
    
    def ID(self):
        return self.point_id
    
    def toPointF(self):
        return QPointF(self.x(),self.y())
            
    
    
    
            
        
        

class GraphPanel(QGraphicsView):
    def __init__(self, parent = None ):
        self.parent = parent
        QGraphicsView.__init__(self,parent)
        self.scene = QGraphicsScene(self)
        self.scale(0.5,0.5)
        self.frame = self.scene.addRect(-20,-20,1044,808)
        self.setScene(self.scene)
        self.PointList = [] 
        for i in range(8):
            self.PointList.append(Point(self,self.scene,i))
            
        self.JointList = []

        
        self.CoM = QGraphicsEllipseItem(scene = self.scene)
        self.CoM.setRect(QRectF(-10,-10,20,20))
        self.CoM.setBrush(QBrush(Qt.red))
        
        
        #Koordinatensystem zeichen
        self.Origin = QGraphicsEllipseItem(scene = self.scene)
        self.Origin.setRect(QRectF(-5,-5,10,10))
        self.Origin.setBrush(QBrush(Qt.black))
        self.Origin.setPos(500,500) 
        self.scene.addLine(QLineF(500,500,700,500),QPen(Qt.red))      
        self.scene.addLine(QLineF(500,500,500,300),QPen(Qt.green)) 
    def redraw(self,newPointList, newJointList, newCoM = None):
        
        
        for i in range(8):
            if(newPointList[i] == None):
                if self.PointList[i].isSelected():

                    self.PointList[i].wasSelected = True
                self.PointList[i].hide()   


            else:
                self.PointList[i].setPos(newPointList[i])
                self.PointList[i].setVisible(True)
                if self.PointList[i].wasSelected:
                    self.PointList[i].setSelected(True)
                    self.PointList[i].wasSelected = False  
                    
        #UpdateJointList
        for oldJoint in self.JointList:
            self.scene.removeItem(oldJoint)
        del self.JointList
        self.JointList = []
        for joint in newJointList:
            PointA = self.PointList[list(joint[0])[0]].toPointF()
            PointB = self.PointList[list(joint[0])[1]].toPointF()
            tmp = QGraphicsLineItem(QLineF(PointA, PointB), scene = self.scene)
            tmp.setPen(QPen(QBrush(Qt.black),joint[2]*100))
            self.JointList.append(tmp)
            del tmp
       
        #Update CoM
        if(newCoM != None):
            self.CoM.setVisible(True)
            self.CoM.setPos(newCoM.toPointF())
        else:
            self.CoM.setVisible(False)
            
    def setReferencePoint(self,ReferencePoint,oldRefPoint = None):
        if not ReferencePoint == None:
            self.PointList[ReferencePoint].setRect(-15,-15,30,30)
        if not oldRefPoint == None:
            self.PointList[oldRefPoint].setRect(-10,-10,20,20)

    
    def setRecFrame(self, Recording = False):
        if Recording:
            Pen = QPen(Qt.red)
            Pen.setWidth(5)
        else:
            Pen = QPen(Qt.black)
            Pen.setWidth(1)
            
        self.frame.setPen(Pen)
class Cylinder(QGraphicsLineItem):


    def __init__(self, PointA, PointB  , Radius , scene):
        Line = QLineF(PointA ,PointB)
        QGraphicsLineItem.__init__(self,Line, scene= scene)
        
        self.setPen(QPen(QBrush(Qt.black),Radius*100))

    def getMiddle(self):

        return QVector2D(0.5*(self.line().x1()+self.line().x2()),0.5*(self.line().y1()+self.line().y2()))


        
    
 

 
        