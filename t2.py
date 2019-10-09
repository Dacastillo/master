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
S2 = np.sqrt(0.2)*a
print(Hjc)
print(S1)
print(S2)

