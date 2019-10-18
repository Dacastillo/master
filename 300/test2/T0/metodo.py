from matplotlib.pyplot import *
import numpy as np
from scipy.linalg import expm
import math as math
nex=4
sigmas = np.kron(np.array([[0,1],[0 for i in range(2)]]),np.eye(nex))
sigmen = sigmas.transpose()
def a(x):
    mat = np.array([[0 for i in range(x)] for j in range(x)])
    acum=0
    for y in range(1,x):
        acum=acum+1
        mat[y-1][y]=float(math.sqrt(acum))
    return(mat)
a = np.kron(np.eye(2),a(nex))
adag = a.transpose()
Hjc = np.matmul(sigmas,sigmen)+np.matmul(adag,a)+(np.matmul(adag,sigmen)+np.matmul(a,sigmas))/1000
e1 = np.array([0,1,0,0,0,0,0,0])
d1 = np.array([[0 for i in range(2*nex)],e1,[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)]])
S1 = np.sqrt(0.1)*sigmen
S1d = S1.transpose()
S2 = np.sqrt(0.2)*a
S2d = S2.transpose()
Hju = Hjc-0.5j*(np.matmul(S1d,S1)+np.matmul(S2d,S2))
ene=500
nst=300
emas_gg=[]
eqju_gg=[]
eqav_gg=[0 for i in range(ene)]
emas_ee=[]
eqju_ee=[]
eqav_ee=[0 for i in range(ene)]
emas_00=[]
eqju_00=[]
eqav_00=[0 for i in range(ene)]
emas_11=[]
eqju_11=[]
eqav_11=[0 for i in range(ene)]

deltat=5/ene
tiempo=[deltat*i for i in range (ene)]
#ecuacion maestra
for i in range (0,ene):
    mat = d1
    mat = mat -deltat*1j*( np.matmul(Hjc,mat)- np.matmul(mat,Hjc) )
    mat = mat +deltat*0.5*( 2*np.matmul(S1,np.matmul(mat,S1d)) -1*np.matmul(mat,np.matmul(S1d,S1)) -1*np.matmul(S1d,np.matmul(S1,mat)) )
    mat = mat +deltat*0.5*( 2*np.matmul(S2,np.matmul(mat,S2d)) -1*np.matmul(mat,np.matmul(S2d,S2)) -1*np.matmul(S2d,np.matmul(S2,mat)) )
    d1 = mat
    emas_gg.append(np.abs(np.matmul(mat,np.matmul(sigmas,sigmen)).trace()))
    emas_ee.append(np.abs(np.matmul(mat,np.matmul(sigmen,sigmas)).trace()))
    emas_00.append(np.abs(np.matmul(mat,np.matmul(adag,a)).trace()))
    emas_11.append(np.abs(np.matmul(mat,np.matmul(a,adag)).trace()))

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
           if(rn2<=(deltap1/deltasum)):
              vec=tongo(np.matmul(S1,vec))
           else:
              vec=tongo(np.matmul(S2,vec))
        else:
           vec=tongo(np.matmul(expm(-1j*deltat*Hju),vec))
        aver_gg= np.matmul(sigmen,vec)
        aver_ee= np.matmul(sigmas,vec)
        aver_00= np.matmul(a,vec)
        aver_11= np.matmul(adag,vec)
        eqju_gg.append(np.abs(np.dot(aver_gg,aver_gg)))
        eqju_ee.append(np.abs(np.dot(aver_ee,aver_ee)))
        eqju_00.append(np.abs(np.dot(aver_00,aver_00)))
        eqju_11.append(np.abs(np.dot(aver_11,aver_11)))
        e1 = vec
        eqav_gg[n]=eqav_gg[n]+(np.abs(np.dot(aver_gg,aver_gg)))/nst
        eqav_ee[n]=eqav_ee[n]+(np.abs(np.dot(aver_ee,aver_ee)))/nst
        eqav_00[n]=eqav_00[n]+(np.abs(np.dot(aver_00,aver_00)))/nst
        eqav_11[n]=eqav_11[n]+(np.abs(np.dot(aver_11,aver_11)))/nst
    e1 = np.array([0,1,0,0,0,0,0,0])

figure()
plot(tiempo,emas_gg)
plot(tiempo,eqav_gg)
savefig('pobg.png')

figure()
plot(tiempo,emas_ee)
plot(tiempo,eqav_ee)
savefig('pobe.png')

figure()
plot(tiempo,emas_00)
plot(tiempo,eqav_00)
savefig('pob0.png')

figure()
plot(tiempo,emas_11)
plot(tiempo,eqav_11)
savefig('pob1.png')
