'''
Created on 05.05.2014

@author: martin
'''

from MainProgramm import Homography, HomPoint
import csv
from numpy import matrix, savetxt, array, zeros, mean
from matplotlib.pyplot import * 
def HomInv(hompoint):
    return (hompoint.item(0)/hompoint.item(2),hompoint.item(1)/hompoint.item(2))
#Messung SO

##Kalibirerung der Daten

#Bildpunkte 

UnitKS = [(0,0),(-1,0),(0,1),(-1,-1)] #Koordinaten Einheitsvektoren 

MOTE_A = 0
MOTE_B = 1

# Kamera Koordinaten der UNITKS Punkte

Urbilder = [None,None]
Urbilder[MOTE_A] = [(609.,142.),(465.,136.),(592.,289.),(447,288)]# <-- Andere Werte hier eintragen
Urbilder[MOTE_B] = [(552.,197.),(400.,190.),(520.,344.),(376,336)]# <-- Andere Werte hier eintragen


#Berechnung der Homographie Matrizen
H_A = Homography(Urbilder[MOTE_A], UnitKS)

H_B = Homography(Urbilder[MOTE_B], UnitKS)

#H_A = matrix([[1,0,0],[0,1,0],[0,0,1]])
# Import Data

Frames = []
with open('MessungSON/messung1.csv') as data:
    reader = csv.reader(data, delimiter = ',')
    i = 0
    for row in reader:
        line = []
        i = i+1
        print i
        for j in range(8):
            j=j*2
            if  row[j] != '':         
                line.append(matrix([float(row[j]),float(row[j+1]),1]).T)
            else:
                line.append(None)  
        Frames.append(line)

    
# Daten Normaliosieren

for Frame in Frames:
    for i in range(4):
        if not Frame[i] is None:
            Frame[i] = HomInv(H_A*Frame[i])
        else:
            Frame[i] = None
        if not Frame[4+i] is None:
            Frame[4+i] = HomInv(H_B*Frame[i+4])
        else:
            Frame[4+i] = None 
 
 


for Frame in Frames[:100]:
    for point in Frame:
        if not point is None:
            plot(point[0],point[1],'x')

origin = HomInv(H_A*matrix([609.,142.,1]).T)
xachse = HomInv(H_A*matrix([465.,136.,1]).T)
yachse = HomInv(H_A*matrix([592.,289.,1]).T)
print yachse
plot(origin[0],origin[1],'ob')
plot(xachse[0],xachse[1], 'or')
plot(yachse[0],yachse[1], 'og')
show()  

# Gleiche Messpunkte Zusammenfassen
# durch Mittelwertsbildung


#Punktkorresondenzen festlegen
data = zeros((4,len(Frames)))
connect = [4,5,6,7] ## Hier festlegen
i = 0 
for Frame in Frames:
    for j in range(4):
        data[j][i] = mean([Frame[i],Frame[connect[i]]].remove(None))
    i+=1
             
