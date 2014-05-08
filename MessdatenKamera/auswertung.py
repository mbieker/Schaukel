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


'Zeiten nachladen'
time = loadtxt('Fuss', usecols=[0])
time = time-time[0]
anz_frames = len(time)

' Aufhaengepunkt festlegen'

AP = HomInv(Trafo*matrix([1.333e1,3.221e2,1]).T)


CoM = zeros((anz_frames,2))

m_ges = 64.5 # kg

def vol_kugel(U):
    r = U/(2*pi)
    return 4*pi*r**3/3

def vol_zylinder(U, l):
    r = U/(2*pi)
    return l*pi*r**2
vol_kopf = vol_kugel(0.55)
vol_to = vol_zylinder(0.80, .65)
vol_ua = 2*vol_zylinder(.23, 0.30)
vol_oa = 2*vol_zylinder(.275, .30)
vol_os = 2*vol_zylinder(.455, .36)
vol_us = 2*vol_zylinder(.29, .5)
vol_ges = vol_kopf + vol_to + vol_ua + vol_oa + vol_os + vol_us
rho = m_ges/vol_ges


m = array([vol_ua,vol_oa,vol_to,vol_os,vol_us,vol_kopf])*rho #Massen der Zyinder

endP = [3,4,2,1,5,0]
print anz_frames

for i in range(anz_frames):
    #Berechnung des Schwerpunktes
    for j in range(5):
        a = array(Points[endP[j]][i])
        b = array(Points[endP[j+1]][i])        
        CoM[i] += 0.5*m[j]*(a+b)
    a = array(Points[6][i])    
    CoM[i] += m[5]*a
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





import matplotlib.animation as animation

fig, (ax1, ax2) = subplots(2,1)

x = [0,0,1,1]    
y= [0,1,1,2]
ax1.set_ylim(-0.2,1.5)
ax1.set_xlim(-1,3)
ax2.plot(time,sqrt(R_quad)-sqrt(R_quad[0]))
    # x-array
body , = ax1.plot([],[],'o-')
head, = ax1.plot([],[],"ro")
SP, = ax1.plot([],[],'gx')
timer, =  ax2.plot([],[],'r-')
ax1.plot([CoM[0][0],CoM[0][0]],[-.2,1.5],'--')
ax2.set_xlabel("Zeit [s]")
ax2.set_ylabel(r"$\Delta r$ [m]")
kopf = Points[6]
hand = Points[3]
ellenbogen = Points[4]
schulter =Points[2]
becken =Points[1]
knie=Points[5]
fuss=Points[0]
print hand[3][0]
def animate(i):
    body.set_data([hand[i][0],ellenbogen[i][0],schulter[i][0],becken[i][0],knie[i][0],fuss[i][0]],[hand[i][1],ellenbogen[i][1],schulter[i][1],becken[i][1],knie[i][1],fuss[i][1]])  # update the data
    head.set_data([kopf[i][0]],[kopf[i][1]])
    timer.set_data([time[i],time[i]],[-.2,.3])
    SP.set_data(CoM[i][0],CoM[i][1])
    return body,head

#Init only required for blitting to give a clean slate.
def init():
    body.set_data([hand[0][0],ellenbogen[0][0],schulter[0][0],becken[0][0],knie[0][0],fuss[0][0]],[hand[0][1],ellenbogen[0][1],schulter[0][1],becken[0][1],knie[0][1],fuss[0][1]])
    head.set_data([kopf[0][0]],[kopf[0][1]])
    CoM[0][0],CoM[0][1]    
    timer.set_data([0,0],[-.2,.3])
    return body, head

ani = animation.FuncAnimation(fig, animate, np.arange(1, 1600), init_func=init,
    interval=50, repeat=True)

ani.save("camera.mp4")
