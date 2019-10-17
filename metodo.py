from matplotlib.pyplot import *
import numpy as np
from scipy.linalg import expm
sigmas = np.array([[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
sigmen = sigmas.transpose()
a = np.array([[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,1,0]])
adag = a.transpose()
Hjc = np.matmul(sigmas,sigmen)+np.matmul(adag,a)+(np.matmul(adag,sigmen)+np.matmul(a,sigmas))/1000
e1 = np.array([0,1,0,0])
d1 = np.array([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])
S1 = np.sqrt(0.1)*sigmen
S1d = S1.transpose()
S2 = np.sqrt(0.2)*a
S2d = S2.transpose()
Hju = Hjc-0.5j*(np.matmul(S1d,S1)+np.matmul(S2d,S2))
ene=500
nst=300
emas=[]
eqju=[]
eqav=[0 for i in range(ene)]
deltat=5/ene
tiempo=[deltat*i for i in range (ene)]
#ecuacion maestra
for i in range (0,ene):
    mat = d1
    mat = mat -deltat*1j*( np.matmul(Hjc,mat)- np.matmul(mat,Hjc) )
    mat = mat +deltat*0.5*( 2*np.matmul(S1,np.matmul(mat,S1d)) -1*np.matmul(mat,np.matmul(S1d,S1)) -1*np.matmul(S1d,np.matmul(S1,mat)) )
    mat = mat +deltat*0.5*( 2*np.matmul(S2,np.matmul(mat,S2d)) -1*np.matmul(mat,np.matmul(S2d,S2)) -1*np.matmul(S2d,np.matmul(S2,mat)) )
    d1 = mat
    emas.append(np.abs(np.matmul(mat,np.matmul(sigmas,sigmen)).trace()))
#quantum jumps
for m in range(0,nst):
    for n in range(0,ene):
        vec = e1
        aver = np.array([0,0,0,0])
        rn1=np.random.random_sample()
        rn2=np.random.random_sample()
        deltap1= deltat*np.abs(np.dot(np.matmul(S1,vec),np.matmul(S1,vec)))
        deltap2= deltat*np.abs(np.dot(np.matmul(S2,vec),np.matmul(S2,vec)))
        def tongo(v): #normalización de vectores
            norm = np.linalg.norm(v)
            if (norm == 0):
               return v
            else:
               return v/norm
        if(deltap1+deltap2==0): #evitar que la normalización se indefina si ambos deltap son 0
          deltasum = 0.001
        else:
          deltasum = deltap1+deltap2
        if(rn1<deltasum):
           if(rn2>=(deltap2/deltasum)):
              vec=tongo(np.matmul(S1,vec))
           else:
              vec=tongo(np.matmul(S2,vec))
        else:
           vec=tongo(vec-np.matmul(expm(-1j*deltat*Hju),vec))
        aver= np.matmul(sigmen,vec)
        eqju.append(np.abs(np.dot(aver,aver)))
        e1 = vec
        eqav[n]=eqav[n]+(np.abs(np.dot(aver,aver)))/nst
    e1 = np.array([0,1,0,0])
print(eqav)
plot(tiempo,emas)
plot(tiempo,eqav)
show()
