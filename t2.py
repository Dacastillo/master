from matplotlib.pyplot import *
import numpy as np
sigmas = np.array([[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
sigmen = sigmas.transpose()
a = np.array([[0,1,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]])
adag = a.transpose()
Hjc = sigmas.dot(sigmen)+ adag.dot(a)+(adag.dot(sigmen)+a.dot(sigmas))/1000
e1 = np.array([0,1,0,0])
d1 = np.array([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])
S1 = np.sqrt(0.1)*sigmen
S1d = S1.transpose()
S2 = np.sqrt(0.2)*a
S2d = S2.transpose()
print(Hjc)
print(S1)
print(S2)
mat = d1
print('ecuacion maestra')
for i in range (0,100):
    mat = mat -0.000000000000000065*(0.05j*(Hjc.dot(d1)-d1.dot(Hjc)))
    mat = mat +0.000000000000000065*(2*S1d.dot(S1.dot(d1))+2*d1.dot(S1d.dot(S1))-S1.dot(d1.dot(S1d)))
    mat = mat +0.000000000000000065*(2*S2d.dot(S2.dot(d1))+2*d1.dot(S2d.dot(S2))-S2.dot(d1.dot(S2d)))
    print(mat[0][0],mat[1][1],mat[2][2],mat[3][3]) 
print('quantum jumps')
a=np.random.random_sample()
b=np.random.random_sample()
print(a,b)
