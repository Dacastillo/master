from matplotlib.pyplot import *
import numpy as np
from scipy.linalg import expm
import math as math
nex=12
sigmas = np.kron(np.array([[0,1],[0,0]]),np.eye(nex))
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
e1 = np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
d1 = np.array([[0 for i in range(2*nex)],e1,[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)],[0 for i in range(2*nex)]])
temp = 10
S1 = np.sqrt(temp+1)*np.sqrt(0.1)*sigmen
S1d =S1.transpose()
S2 = np.sqrt(temp+1)*np.sqrt(0.2)*a
S2d =S2.transpose()
S3 = np.sqrt(temp)*np.sqrt(0.1)*sigmas
S3d =S3.transpose()
S4 = np.sqrt(temp)*np.sqrt(0.2)*adag
S4d =S4.transpose()
Hju = Hjc-0.5j*(np.matmul(S1d,S1)+np.matmul(S2d,S2)+np.matmul(S3d,S3)+np.matmul(S4d,S4))
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

deltat=50/ene
tiempo=[deltat*i for i in range (ene)]
def mulmat(a,b):
    c=a.dot(b)
    return c
#ecuacion maestra
for i in range (0,ene):
    mat = d1
    mat = mat -deltat*1j*( mulmat(Hjc,mat)- mulmat(mat,Hjc) )
    mat = mat +deltat*0.5*( 2*mulmat(S1,mulmat(mat,S1d)) -1*mulmat(mat,mulmat(S1d,S1)) -1*mulmat(S1d,mulmat(S1,mat)) )
    mat = mat +deltat*0.5*( 2*mulmat(S2,mulmat(mat,S2d)) -1*mulmat(mat,mulmat(S2d,S2)) -1*mulmat(S2d,mulmat(S2,mat)) )
    mat = mat +deltat*0.5*( 2*mulmat(S3,mulmat(mat,S3d)) -1*mulmat(mat,mulmat(S3d,S3)) -1*mulmat(S3d,mulmat(S3,mat)) )
    mat = mat +deltat*0.5*( 2*mulmat(S4,mulmat(mat,S4d)) -1*mulmat(mat,mulmat(S4d,S4)) -1*mulmat(S4d,mulmat(S4,mat)) )
    d1 = mat
    emas_gg.append(np.abs(mulmat(mat,mulmat(sigmas,sigmen)).trace()))
    emas_ee.append(np.abs(mulmat(mat,mulmat(sigmen,sigmas)).trace()))
    emas_00.append(np.abs(mulmat(mat,mulmat(adag,a)).trace()))
    emas_11.append(np.abs(mulmat(mat,mulmat(a,adag)).trace()))

#quantum jumps
for m in range(0,nst):
    for n in range(0,ene):
        vec = e1
        aver = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        rn1=np.random.random_sample()
        rn2=np.random.random_sample()
        deltap1= deltat*np.abs(np.dot(np.array(mulmat(S1,vec)),np.array(mulmat(S1,vec))))
        deltap2= deltat*np.abs(np.dot(np.array(mulmat(S2,vec)),np.array(mulmat(S2,vec))))
        deltap3= deltat*np.abs(np.dot(np.array(mulmat(S3,vec)),np.array(mulmat(S3,vec))))
        deltap4= deltat*np.abs(np.dot(np.array(mulmat(S4,vec)),np.array(mulmat(S4,vec))))
        def tongo(v): #normalización de vectores
            norm = np.linalg.norm(v)
            if (norm == 0):
               return v
            else:
               return v/norm
        if(deltap1+deltap2+deltap3+deltap4==0): #evitar que la normalización se indefina si ambos deltap son 0
          deltasum = 0.001
        else:
          deltasum = deltap1+deltap2+deltap3+deltap4
        if(rn1<deltasum):
           if(rn2<=(deltap1/deltasum)):
              vec=tongo(mulmat(S1,vec))
           elif(rn2<=((deltap1+deltap2)/deltasum)):
              vec=tongo(mulmat(S2,vec))
           elif(rn2<=((deltap1+deltap2+deltap3)/deltasum)):
              vec=tongo(mulmat(S3,vec))
           else:
              vec=tongo(mulmat(S4,vec))
        else:
           vec=tongo(mulmat(expm(-1j*deltat*Hju),vec))
        aver_gg= mulmat(sigmen,vec)
        aver_ee= mulmat(sigmas,vec)
        aver_00= mulmat(a,vec)
        aver_11= mulmat(adag,vec)
        eqju_gg.append(np.abs(np.dot(aver_gg,aver_gg)))
        eqju_ee.append(np.abs(np.dot(aver_ee,aver_ee)))
        eqju_00.append(np.abs(np.dot(aver_00,aver_00)))
        eqju_11.append(np.abs(np.dot(aver_11,aver_11)))
        e1 = vec
        eqav_gg[n]=eqav_gg[n]+(np.abs(np.dot(aver_gg,aver_gg)))/nst
        eqav_ee[n]=eqav_ee[n]+(np.abs(np.dot(aver_ee,aver_ee)))/nst
        eqav_00[n]=eqav_00[n]+(np.abs(np.dot(aver_00,aver_00)))/nst
        eqav_11[n]=eqav_11[n]+(np.abs(np.dot(aver_11,aver_11)))/nst
    e1 = np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

figure()
plot(tiempo,emas_gg)
plot(tiempo,eqav_gg)
savefig('pobg.png')

figure()
plot(tiempo,emas_00)
plot(tiempo,eqav_00)
savefig('pob0.png')

