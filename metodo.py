from matplotlib.pyplot import *
import numpy as np
sigmas = np.array([[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
sigmen = sigmas.transpose()
a = np.array([[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,1,0]])
adag = a.transpose()
Hjc = sigmas.dot(sigmen)+ adag.dot(a)+(adag.dot(sigmen)+a.dot(sigmas))/1000
e1 = np.array([0,1,0,0])
d1 = np.array([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])
S1 = np.sqrt(0.1)*sigmen
S1d = S1.transpose()
S2 = np.sqrt(0.2)*a
S2d = S2.transpose()
ene=100
emas=[]
eqju=[]
deltat=5/ene
tiempo=[deltat*i for i in range (ene)]
#ecuacion maestra
for i in range (0,ene):
    mat = d1
    mat = mat -deltat*(1j*(np.tensordot(Hjc,mat,0)-np.tensordot(mat,Hjc,0)))
    mat = mat +deltat*(S1.dot(mat.dot(S1d))-0.5*mat.dot(S1d.dot(S1))-0.5*S1d.dot(S1.dot(mat)))
    mat = mat +deltat*(S2.dot(mat.dot(S2d))-0.5*mat.dot(S2d.dot(S2))-0.5*S2d.dot(S2.dot(mat)))
    d1 = mat
    emas.append(np.absolute(mat.dot(sigmen.dot(sigmas)).trace())) 
#quantum jumps
for i in range (0,ene):
    vec = e1
    rn1=np.random.random_sample()
    rn2=np.random.random_sample()
    deltap1=deltat*np.abs(np.dot(S1.dot(vec),S1.dot(vec)))
    deltap2=deltat*np.abs(np.dot(S2.dot(vec),S2.dot(vec)))
    def tongo(v):
        norm = np.linalg.norm(v)
        if (norm == 0):
           return v
        else:
           return v/norm    
    print(rn1,rn2,deltap1,deltap2)
    if(rn1<=0.5):
       if(rn2<=0.2):
           vec=tongo(S1.dot(vec))
       else:
            vec=tongo(S2.dot(vec))   
    else:
       vec=tongo(vec-1j*deltat*(Hjc.dot(vec)-0.5j*(S1d.dot(S1)+S2d.dot(S2))))
    e1 = vec
    eqju.append(np.absolute(np.dot(sigmas.dot(vec),sigmas.dot(vec))))
#print(eqju)
#plot(tiempo,emas)
#plot(tiempo,eqju)
#show()
