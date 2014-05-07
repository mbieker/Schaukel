from numpy import *
from matplotlib.pyplot import *
from __builtin__ import len

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

    X = linalg.solve(A,B)
    m11 = X.item(0)
    m12 = X.item(1)
    m13 = X.item(2)
    m21 = X.item(3)
    m22 = X.item(4)
    m23 = X.item(5)
    m31 = X.item(6)
    m32 = X.item(7)
    return matrix([[m11,m12,m13],[m21,m22,m23],[m31,m32,1]])


def HomInv(p):
    return  [p.item(0),p.item(1)/p.item(2)]



# Define Homography

#unit =   [(0,0),(3.12,0),(0,1.20),(3.12,1.20)]
#bilder = [(-1.538e2,-1.068e1),(1.317e2,2.545e1),(-3.271e2,1.987e2),(1.254e2,2.191e2)]
unit =   [(0,0),(1.16,0),(0.44,1.89),(0.66,1.89)]
bilder = [(-2.299e2,-9.404e1),(-12.02,-69.76),(-1.538e2,3.044e2),(-1.138e2,3.044e2)]
Trafo = Homography(   bilder , unit)
#Trafo = identity(3)

print Trafo

# Import Data 
filenames = ['Fuss', 'Becken', 'Schulter', 'Hand', 'Ellenbogen','Knie', 'Kopf', 'Sitz']

Points = [[],[],[],[],[],[],[],[]]
i = 0

Points = zeros((8,2000,2))
for file in filenames:

    data = loadtxt(file, usecols=[1,2])
    
    j = 0
    for Frame in data:
        tmp = HomInv(Trafo*matrix(list(Frame)+[1]).T)
        Points[i][j][0]= tmp[0]
        Points[i][j][1] = tmp[1]
        j += 1
    i += 1

Points = array(Points)
print Points.T[:3]

'Zeiten nachladen'
time = loadtxt('Fuss', usecols=[0])
time = time-time[0]
anz_frames = len(time)

' Aufhaengepunkt festlegen'

AP = HomInv(Trafo*matrix([1.333e1,3.221e2,1]).T)


CoM = zeros((anz_frames,2))

m_ges = 64.5 # kg

vol_kopf = 1.0/6*0.55**3/pi*2
vol_to = 0.65*pi*(0.8/(2*pi))**2
vol_ua = .3*pi*(.23/(2*pi))**2
vol_oa = .3*pi*(.275/(2*pi))**2
vol_os = 0.36*pi*(.455/(2*pi))**2
vol_us = .5*pi*(.29/(2*pi))**2
vol_ges = vol_kopf+vol_os+vol_us+vol_ua+ vol_oa+vol_kopf+vol_to
rho = m_ges/vol_ges


# Angaben des Zylinders-- Anfang und Ende-- Masse -- Radius
m = array([vol_ua,vol_oa,vol_to,vol_os,vol_us])*rho #Massen der Zyinder
r = array([1]*5) #Radien der Zylinder
endP = [3,4,2,1,5,0]


for i in range(anz_frames):
    #Berechnung des Schwerpunktes
    for j in range(5):
        a = array(Points[endP[j]][i])
        b = array(Points[endP[j+1]][i])        
        CoM[i] += 0.5*m.item(j)*(a+b)
    CoM[i] = CoM[i]/m_ges

V_CoM = zeros((anz_frames,2))
for i in range(1,anz_frames-1):
    V_CoM[i][0]= (CoM[i+1][0]-CoM[i-1][0])/(0.0222)
    V_CoM[i][1]= (CoM[i+1][1]-CoM[i-1][1])/(0.0222)
''' Winkelgeschindigkeit als Kreuprodukt aus vektor vom CoM zur Schaukelaufhaengung r x V / r**2
'''
R = CoM-AP
R_quad = array([r[0]**2+r[1]**2 for r in R])

omega = zeros(anz_frames)

for i in range(1,anz_frames-1):
    omega[i] = (R[i][0]*V_CoM[i][1] - R[i][1]*V_CoM[i][0])/ R_quad[i]
    
CoMx = CoM.T[0]
CoMy = CoM.T[1]

V_ges = array([sqrt(v[0]**2+v[1]**2) for v in V_CoM])

#plot(time,sqrt(R_quad)-sqrt(R_quad[0]))
plot(CoMx,CoMy,'x')


show()


        

