from qutip import * #Liberia qutip
from matplotlib.pyplot import * #Libreria matplotlib
import numpy as np #Liberia numpy
times = np.linspace(0,5,100) #definir intervalo temporal 
I1 =  (1/(np.sqrt(2)))*(tensor(basis(2,0),basis(2,0))+tensor(basis(2,1),basis(2,1)))#Definir estado inicial Bell 1
I2 =  (1/(np.sqrt(2)))*(tensor(basis(2,0),basis(2,1))+tensor(basis(2,1),basis(2,0)))#Definir estado inicial Bell 3
I3 =  tensor(basis(2,0),basis(2,1))#Definir estado inicial logico 01
I4 =  tensor(basis(2,1),basis(2,1))#Definir estado inicial logico 11
I5 =  tensor(basis(2,0),basis(2,0))#Definir estado inicial logico 00
sigmen1 = tensor(sigmam(),identity(2)) #Sigma menos en sistema 1
sigmas1 = tensor(sigmap(),identity(2)) #Sigma mas en sistema 1 
sigmen2 = tensor(identity(2),sigmam()) #Sigma menos en sistema 2
sigmas2 = tensor(identity(2),sigmap()) #Sigma mas en sistema 2
em_I1_S0C = mesolve(tensor(identity(2),identity(2)), I1, times, [sigmen1+sigmen2])  #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios con interaccion
em_I2_S0C = mesolve(tensor(identity(2),identity(2)), I2, times, [sigmen1+sigmen2])  #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios con interaccion
em_I3_S0C = mesolve(tensor(identity(2),identity(2)), I3, times, [sigmen1+sigmen2])  #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios con interaccion
em_I4_S0C = mesolve(tensor(identity(2),identity(2)), I4, times, [sigmen1+sigmen2])  #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios con interaccion
em_I5_S0C = mesolve(tensor(identity(2),identity(2)), I5, times, [sigmen1+sigmen2])  #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios con interaccion
em_I1_S1C = mesolve(tensor(identity(2),identity(2)), I1, times, [np.sqrt(1.1)*sigmen1+np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales con tinteraccion
em_I2_S1C = mesolve(tensor(identity(2),identity(2)), I2, times, [np.sqrt(1.1)*sigmen1+np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales con interaccion
em_I3_S1C = mesolve(tensor(identity(2),identity(2)), I3, times, [np.sqrt(1.1)*sigmen1+np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales con interaccion
em_I4_S1C = mesolve(tensor(identity(2),identity(2)), I4, times, [np.sqrt(1.1)*sigmen1+np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales con interaccion
em_I5_S1C = mesolve(tensor(identity(2),identity(2)), I5, times, [np.sqrt(1.1)*sigmen1+np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales con interaccion
em_I1_S2C = mesolve(tensor(identity(2),identity(2)), I1, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1+np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos con interaccion
em_I2_S2C = mesolve(tensor(identity(2),identity(2)), I2, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1+np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos con interaccion
em_I3_S2C = mesolve(tensor(identity(2),identity(2)), I3, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1+np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos con interaccion
em_I4_S2C = mesolve(tensor(identity(2),identity(2)), I4, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1+np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos con interaccion
em_I5_S2C = mesolve(tensor(identity(2),identity(2)), I5, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1+np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos con interaccion
em_I1_S0S = mesolve(tensor(identity(2),identity(2)), I1, times, [sigmen1,sigmen2]) #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios sin interaccion
em_I2_S0S = mesolve(tensor(identity(2),identity(2)), I2, times, [sigmen1,sigmen2]) #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios sin interaccion
em_I3_S0S = mesolve(tensor(identity(2),identity(2)), I3, times, [sigmen1,sigmen2]) #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios sin interaccion
em_I4_S0S = mesolve(tensor(identity(2),identity(2)), I4, times, [sigmen1,sigmen2]) #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios sin interaccion
em_I5_S0S = mesolve(tensor(identity(2),identity(2)), I5, times, [sigmen1,sigmen2]) #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios sin interaccion
em_I1_S1S = mesolve(tensor(identity(2),identity(2)), I1, times, [np.sqrt(1.1)*sigmen1,np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1,np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales sin interaccion
em_I2_S1S = mesolve(tensor(identity(2),identity(2)), I2, times, [np.sqrt(1.1)*sigmen1,np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1,np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales sin interaccion
em_I3_S1S = mesolve(tensor(identity(2),identity(2)), I3, times, [np.sqrt(1.1)*sigmen1,np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1,np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales sin interaccion
em_I4_S1S = mesolve(tensor(identity(2),identity(2)), I4, times, [np.sqrt(1.1)*sigmen1,np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1,np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales sin interaccion
em_I5_S1S = mesolve(tensor(identity(2),identity(2)), I5, times, [np.sqrt(1.1)*sigmen1,np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1,np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales sin interaccion
em_I1_S2S = mesolve(tensor(identity(2),identity(2)), I1, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1,np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos sin interaccion
em_I2_S2S = mesolve(tensor(identity(2),identity(2)), I2, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1,np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos sin interaccion
em_I3_S2S = mesolve(tensor(identity(2),identity(2)), I3, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1,np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos sin interaccion
em_I4_S2S = mesolve(tensor(identity(2),identity(2)), I4, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1,np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos sin interaccion
em_I5_S2S = mesolve(tensor(identity(2),identity(2)), I5, times, [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1,np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos sin interaccion
tiempo = [(1/20)*i for i in range(100)]#Intervalo de tiempo para los gráficos
#Reservorio vacío sin interacción
conc_I1_S0S=[0 for i in range(100)]
disc_I1_S0S=[0 for i in range(100)]
conc_I2_S0S=[0 for i in range(100)]
disc_I2_S0S=[0 for i in range(100)]
conc_I3_S0S=[0 for i in range(100)]
disc_I3_S0S=[0 for i in range(100)]
conc_I4_S0S=[0 for i in range(100)]
disc_I4_S0S=[0 for i in range(100)]
conc_I5_S0S=[0 for i in range(100)]
disc_I5_S0S=[0 for i in range(100)]

for i in range (0,100):
      mat=Qobj(em_I1_S0S.states[i])
      c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
      c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
      c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
      print (c1,c2,c3)
      consar=np.array([c1,c2,c3])
      c=np.amax(consar)
      conc_I1_S0S[i]=concurrence(mat)
      disc_I1_S0S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
      mat=Qobj(em_I2_S0S.states[i])
      c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
      c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
      c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
      print (c1,c2,c3)
      consar=np.array([c1,c2,c3])
      c=np.amax(consar)
      conc_I2_S0S[i]=concurrence(mat)
      disc_I2_S0S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
      mat=Qobj(em_I3_S0S.states[i])
      c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
      c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
      c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
      print (c1,c2,c3)
      consar=np.array([c1,c2,c3])
      c=np.amax(consar)
      conc_I3_S0S[i]=concurrence(mat)
      disc_I3_S0S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
      mat=Qobj(em_I4_S0S.states[i])
      c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
      c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
      c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
      print(c1,c2,c3)
      consar=np.array([c1,c2,c3])
      c=np.amax(consar)
      conc_I4_S0S[i]=concurrence(mat)
      disc_I4_S0S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
      mat=Qobj(em_I5_S0S.states[i])
      c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
      c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
      c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
      print (c1,c2,c3)
      consar=np.array([c1,c2,c3])
      c=np.amax(consar)
      conc_I5_S0S[i]=concurrence(mat)
      disc_I5_S0S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio térmico sin interacción
conc_I1_S1S=[0 for i in range(100)]
disc_I1_S1S=[0 for i in range(100)]
conc_I2_S1S=[0 for i in range(100)]
disc_I2_S1S=[0 for i in range(100)]
conc_I3_S1S=[0 for i in range(100)]
disc_I3_S1S=[0 for i in range(100)]
conc_I4_S1S=[0 for i in range(100)]
disc_I4_S1S=[0 for i in range(100)]
conc_I5_S1S=[0 for i in range(100)]
disc_I5_S1S=[0 for i in range(100)]
for i in range (0,100):
      mat=Qobj(em_I1_S1S.states[i])
      c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
      c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
      c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
      print (c1,c2,c3)
      consar=np.array([c1,c2,c3])
      c=np.amax(consar)
      conc_I1_S1S[i]=concurrence(mat)
      disc_I1_S1S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I2_S1S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I2_S1S[i]=concurrence(mat)
    disc_I2_S1S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I3_S1S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I3_S1S[i]=concurrence(mat)
    disc_I3_S1S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I4_S1S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I4_S1S[i]=concurrence(mat)
    disc_I4_S1S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    mat=Qobj(em_I5_S1S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I5_S1S[i]=concurrence(mat)
    disc_I5_S1S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio comprimido sin interacción
conc_I1_S2S=[0 for i in range(100)]
disc_I1_S2S=[0 for i in range(100)]
conc_I2_S2S=[0 for i in range(100)]
disc_I2_S2S=[0 for i in range(100)]
conc_I3_S2S=[0 for i in range(100)]
disc_I3_S2S=[0 for i in range(100)]
conc_I4_S2S=[0 for i in range(100)]
disc_I4_S2S=[0 for i in range(100)]
conc_I5_S2S=[0 for i in range(100)]
disc_I5_S2S=[0 for i in range(100)]
for i in range (0,100):
    mat=Qobj(em_I1_S2S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I1_S2S[i]=concurrence(mat)
    disc_I1_S2S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    mat=Qobj(em_I2_S2S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I2_S2S[i]=concurrence(mat)
    disc_I2_S2S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    mat=Qobj(em_I3_S2S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I3_S2S[i]=concurrence(mat)
    disc_I3_S2S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I4_S2S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I4_S2S[i]=concurrence(mat)
    disc_I4_S2S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I5_S2S.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I5_S2S[i]=concurrence(mat)
    disc_I5_S2S[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio vacío con interacción
conc_I1_S0C=[0 for i in range(100)]
disc_I1_S0C=[0 for i in range(100)]
conc_I2_S0C=[0 for i in range(100)]
disc_I2_S0C=[0 for i in range(100)]
conc_I3_S0C=[0 for i in range(100)]
disc_I3_S0C=[0 for i in range(100)]
conc_I4_S0C=[0 for i in range(100)]
disc_I4_S0C=[0 for i in range(100)]
conc_I5_S0C=[0 for i in range(100)]
disc_I5_S0C=[0 for i in range(100)]
for i in range (0,100):
    mat=Qobj(em_I1_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I1_S0C[i]=concurrence(mat)
    disc_I1_S0C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I2_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I2_S0C[i]=concurrence(mat)
    disc_I2_S0C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I3_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I3_S0C[i]=concurrence(mat)
    disc_I3_S0C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I4_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print(c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I4_S0C[i]=concurrence(mat)
    disc_I4_S0C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I5_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I5_S0C[i]=concurrence(mat)
    disc_I5_S0C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio térmico con interacción
conc_I1_S1C=[0 for i in range(100)]
disc_I1_S1C=[0 for i in range(100)]
conc_I2_S1C=[0 for i in range(100)]
disc_I2_S1C=[0 for i in range(100)]
conc_I3_S1C=[0 for i in range(100)]
disc_I3_S1C=[0 for i in range(100)]
conc_I4_S1C=[0 for i in range(100)]
disc_I4_S1C=[0 for i in range(100)]
conc_I5_S1C=[0 for i in range(100)]
disc_I5_S1C=[0 for i in range(100)]
for i in range (0,100):
    mat=Qobj(em_I1_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I1_S1C[i]=concurrence(mat)
    disc_I1_S1C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

    
for i in range (0,100):
    mat=Qobj(em_I2_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I2_S1C[i]=concurrence(mat)
    disc_I2_S1C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I3_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I3_S1C[i]=concurrence(mat)
    disc_I3_S1C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I4_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I4_S1C[i]=concurrence(mat)
    disc_I4_S1C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I5_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I5_S1C[i]=concurrence(mat)
    disc_I5_S1C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio comprimido con interacción
conc_I1_S2C=[0 for i in range(100)]
disc_I1_S2C=[0 for i in range(100)]
conc_I2_S2C=[0 for i in range(100)]
disc_I2_S2C=[0 for i in range(100)]
conc_I3_S2C=[0 for i in range(100)]
disc_I3_S2C=[0 for i in range(100)]
conc_I4_S2C=[0 for i in range(100)]
disc_I4_S2C=[0 for i in range(100)]
conc_I5_S2C=[0 for i in range(100)]
disc_I5_S2C=[0 for i in range(100)]
for i in range (0,100):
    mat=Qobj(em_I1_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I1_S2C[i]=concurrence(mat)
    disc_I1_S2C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    mat=Qobj(em_I2_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I2_S2C[i]=concurrence(mat)
    disc_I2_S2C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    mat=Qobj(em_I3_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I3_S2C[i]=concurrence(mat)
    disc_I3_S2C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I4_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I4_S2C[i]=concurrence(mat)
    disc_I4_S2C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I5_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    conc_I5_S2C[i]=concurrence(mat)
    disc_I5_S2C[i]=mat.eigenenergies()[0]*np.log2(np.absolute(4*mat.eigenenergies()[0]))+mat.eigenenergies()[1]*np.log2(np.absolute(4*mat.eigenenergies()[1]))+mat.eigenenergies()[2]*np.log2(np.absolute(4*mat.eigenenergies()[2]))+mat.eigenenergies()[3]*np.log2(np.absolute(4*mat.eigenenergies()[3]))+0.5*(-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Graficar
figure()
plot(tiempo,disc_I1_S0S)
plot(tiempo,disc_I1_S1S)
plot(tiempo,disc_I1_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell1_S.png')

figure()
plot(tiempo,disc_I2_S0S)
plot(tiempo,disc_I2_S1S)
plot(tiempo,disc_I2_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell3_S.png')

figure()
plot(tiempo,disc_I3_S0S)
plot(tiempo,disc_I3_S1S)
plot(tiempo,disc_I3_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_logi2_S.png')

figure()
plot(tiempo,disc_I4_S0S)
plot(tiempo,disc_I4_S1S)
plot(tiempo,disc_I4_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_logi4_S.png')

figure()
plot(tiempo,disc_I5_S0S)
plot(tiempo,disc_I5_S1S)
plot(tiempo,disc_I5_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('disc_logi1_S.png')

figure()
plot(tiempo,conc_I1_S0S)
plot(tiempo,conc_I1_S1S)
plot(tiempo,conc_I1_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_bell1_S.png')

figure()
plot(tiempo,conc_I2_S0S)
plot(tiempo,conc_I2_S1S)
plot(tiempo,conc_I2_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_bell3_S.png')

figure()
plot(tiempo,conc_I3_S0S)
plot(tiempo,conc_I3_S1S)
plot(tiempo,conc_I3_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi2_S.png')

figure()
plot(tiempo,conc_I4_S0S)
plot(tiempo,conc_I4_S1S)
plot(tiempo,conc_I4_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi4_S.png')

figure()
plot(tiempo,conc_I5_S0S)
plot(tiempo,conc_I5_S1S)
plot(tiempo,conc_I5_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi1_S.png')

figure()
plot(tiempo,disc_I1_S0C)
plot(tiempo,disc_I1_S1C)
plot(tiempo,disc_I1_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell1_C.png')

figure()
plot(tiempo,disc_I2_S0C)
plot(tiempo,disc_I2_S1C)
plot(tiempo,disc_I2_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell3_C.png')

figure()
plot(tiempo,disc_I3_S0C)
plot(tiempo,disc_I3_S1C)
plot(tiempo,disc_I3_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_logi2_C.png')

figure()
plot(tiempo,disc_I4_S0C)
plot(tiempo,disc_I4_S1C)
plot(tiempo,disc_I4_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_logi4_C.png')

figure()
plot(tiempo,disc_I5_S0C)
plot(tiempo,disc_I5_S1C)
plot(tiempo,disc_I5_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('disc_logi1_C.png')

figure()
plot(tiempo,conc_I1_S0C)
plot(tiempo,conc_I1_S1C)
plot(tiempo,conc_I1_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_bell1_C.png')

figure()
plot(tiempo,conc_I2_S0C)
plot(tiempo,conc_I2_S1C)
plot(tiempo,conc_I2_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_bell3_C.png')

figure()
plot(tiempo,conc_I3_S0C)
plot(tiempo,conc_I3_S1C)
plot(tiempo,conc_I3_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi2_C.png')

figure()
plot(tiempo,conc_I4_S0C)
plot(tiempo,conc_I4_S1C)
plot(tiempo,conc_I4_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi4_C.png')

figure()
plot(tiempo,conc_I5_S0C)
plot(tiempo,conc_I5_S1C)
plot(tiempo,conc_I5_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi1_C.png')
