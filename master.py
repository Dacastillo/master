from qutip import * #Liberia qutip
from matplotlib.pyplot import * #Libreria matplotlib
import numpy as np #Liberia numpy
times = np.linspace(0,5, 100) #definir intervalo temporal 
I1 =  (1/(np.sqrt(2)))*(tensor(basis(2,0),basis(2,0))+tensor(basis(2,1),basis(2,1)))#Definir estado inicial Bell 1
I2 =  (1/(np.sqrt(2)))*(tensor(basis(2,0),basis(2,1))+tensor(basis(2,1),basis(2,0)))#Definir estado inicial Bell 3
I3 =  tensor(basis(2,0),basis(2,1))#Definir estado inicial logico 01
I4 =  tensor(basis(2,1),basis(2,1))#Definir estado inicial logico 11
I5 =  tensor(basis(2,0),basis(2,0))#Definir estado inicial logico 00
sigmen1 = tensor(sigmam(),identity(2)) #Sigma menos en sistema 1
sigmas1 = tensor(sigmap(),identity(2)) #Sigma mas en sistema 1 
sigmen2 = tensor(identity(2),sigmam()) #Sigma menos en sistema 2
sigmas2 = tensor(identity(2),sigmap()) #Sigma mas en sistema 2
S0S = [sigmen1,sigmen2]
S1S = [np.sqrt(1.1)*sigmen1,np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1,np.sqrt(0.1)*sigmas2]
S2S = [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1,np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]
S0C = [sigmen1+sigmen2]
S1C = [np.sqrt(1.1)*sigmen1+np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1+np.sqrt(0.1)*sigmas2]
S2C = [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1+np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]
#Definir funcion logaritmo segura
def log_2(x):
    if np.real(x) <= 0:
       return 0
    else:
       return np.log2(x)
#Definir entropia condicional para minimizar
def entropy_cond(a,b,t1,t2):
    e= 0
    if (1-t1)/2 > 0:
       e = e -a*( (1-t1)/2)*log_2( (1-t1)/2 )
    if (1+t1)/2 > 0:
       e = e -a*( (1+t1)/2)*log_2( (1+t1)/2 )
    if (1-t2)/2 > 0:
       e = e -b*( (1-t2)/2)*log_2( (1-t2)/2 )
    if (1+t2)/2 > 0:
       e = e -b*( (1+t2)/2)*log_2( (1+t2)/2 )
    return e
#Definir función entropía binaria con logaritmo seguro
def h_bin(x):
    h=-x*log_2(x)-(1-x)*log_2(1-x)
    return h
#Definir funcion que calcula ecuaciones maestras y evaluar si funciona fuera para los estados lógicos
def me(IN,RES):
    sol=mesolve(tensor(identity(2),identity(2)), IN, times, RES)
    out=[[0 for i in range(100)],[0 for i in range(100)]]
    conc=[0 for i in range(100)]
    disc=[0 for i in range(100)]   
    def entropy_opt(a): #función que optimiza la entropía condicional necesaria para sacar discordia
        ent_comp=[0 for i in range(4)]
        r00= a.matrix_element(tensor(basis(2,0),basis(2,0)).dag(),tensor(basis(2,0),basis(2,0)))
        r11= a.matrix_element(tensor(basis(2,0),basis(2,1)).dag(),tensor(basis(2,0),basis(2,1)))
        r22= a.matrix_element(tensor(basis(2,1),basis(2,0)).dag(),tensor(basis(2,1),basis(2,0)))
        r33= a.matrix_element(tensor(basis(2,1),basis(2,1)).dag(),tensor(basis(2,1),basis(2,1)))
        r03r= np.real(a.matrix_element(tensor(basis(2,0),basis(2,0)).dag(),tensor(basis(2,1),basis(2,1))))
        r12r= np.real(a.matrix_element(tensor(basis(2,0),basis(2,1)).dag(),tensor(basis(2,1),basis(2,0))))
        r03i= np.imag(a.matrix_element(tensor(basis(2,0),basis(2,0)).dag(),tensor(basis(2,1),basis(2,1))))
        r12i= np.imag(a.matrix_element(tensor(basis(2,0),basis(2,1)).dag(),tensor(basis(2,1),basis(2,0))))
        r03a= np.absolute(a.matrix_element(tensor(basis(2,0),basis(2,0)).dag(),tensor(basis(2,1),basis(2,1))))
        r12a= np.absolute(a.matrix_element(tensor(basis(2,0),basis(2,1)).dag(),tensor(basis(2,1),basis(2,0))))
        if r11+r33 == 0:
           ent_comp[0]=1
           ent_comp[1]=1
        elif r00+r22 == 0:
           ent_comp[0]=1
           ent_comp[1]=1
        else:
           ent_comp[0]=entropy_cond( r11+r33, r00+r22, np.absolute((r11-r33)/(r00+r22)),np.absolute((r00-r22)/(r11+r33)) )
           ent_comp[1]=entropy_cond( r00+r22, r11+r33, np.absolute((r00-r22)/(r11+r33)),np.absolute((r11-r33)/(r00+r22)) )
        
        ent_comp[2]=entropy_cond( 0.5, 0.5,  np.sqrt(((r00-r22)+(r11-r33))**2+4*((r03a)**2+(r12a)**2+2*r03r*r12r)), np.sqrt(((r00-r22)+(r11-r33))**2+4*((r03a)**2+(r12a)**2+2*r03r*r12r)))
        ent_comp[3]=entropy_cond( 0.5, 0.5,  np.sqrt(((r00-r22)+(r11-r33))**2+4*((r03a)**2+(r12a)**2+2*r03r*r12r)-4*(r03r*r12r-r03i*r12i)), np.sqrt(((r00-r22)+(r11-r33))**2+4*((r03a)**2+(r12a)**2+2*r03r*r12r)-4*(r03r*r12r-r03i*r12i)))
        e= np.real(np.amin(ent_comp))
        if e <= 0:
           e= 0
        return e
    for i in range (0,100):
        mat=Qobj(sol.states[i])
        conc[i]=concurrence(mat)
        disc[i]=np.absolute(entropy_opt(mat)-entropy_conditional(mat,0))
    out=[conc,disc]
    return out

tiempo = [(1/20)*i for i in range(100)]#Intervalo de tiempo para los gráficos

 
#Graficar
fig, axs = subplots(2,2)
axs[0,0].plot(tiempo,me(I1,S0S)[1], 'r')
axs[0,0].plot(tiempo,me(I1,S1S)[1], 'g')
axs[0,0].plot(tiempo,me(I1,S2S)[1], 'b')
axs[0,1].plot(tiempo,me(I1,S0S)[0], 'r')
axs[0,1].plot(tiempo,me(I1,S1S)[0], 'g')
axs[0,1].plot(tiempo,me(I1,S2S)[0], 'b')
axs[1,0].plot(tiempo,me(I1,S0C)[1], 'r')
axs[1,0].plot(tiempo,me(I1,S1C)[1], 'g')
axs[1,0].plot(tiempo,me(I1,S2C)[1], 'b')
axs[1,1].plot(tiempo,me(I1,S0C)[0], 'r')
axs[1,1].plot(tiempo,me(I1,S1C)[0], 'g')
axs[1,1].plot(tiempo,me(I1,S2C)[0], 'b')
rcParams.update({'font.size': 6})
savefig('bell1.png')

#Graficar
fig, axs = subplots(2,2)
axs[0,0].plot(tiempo,me(I2,S0S)[1], 'r')
axs[0,0].plot(tiempo,me(I2,S1S)[1], 'g')
axs[0,0].plot(tiempo,me(I2,S2S)[1], 'b')
axs[0,1].plot(tiempo,me(I2,S0S)[0], 'r')
axs[0,1].plot(tiempo,me(I2,S1S)[0], 'g')
axs[0,1].plot(tiempo,me(I2,S2S)[0], 'b')
axs[1,0].plot(tiempo,me(I2,S0C)[1], 'r')
axs[1,0].plot(tiempo,me(I2,S1C)[1], 'g')
axs[1,0].plot(tiempo,me(I2,S2C)[1], 'b')
axs[1,1].plot(tiempo,me(I2,S0C)[0], 'r')
axs[1,1].plot(tiempo,me(I2,S1C)[0], 'g')
axs[1,1].plot(tiempo,me(I2,S2C)[0], 'b')
rcParams.update({'font.size': 6})
savefig('bell3.png')


#Graficar
fig, axs = subplots(2,2)
axs[0,0].plot(tiempo,me(I3,S0S)[1], 'r')
axs[0,0].plot(tiempo,me(I3,S1S)[1], 'g')
axs[0,0].plot(tiempo,me(I3,S2S)[1], 'b')
axs[0,1].plot(tiempo,me(I3,S0S)[0], 'r')
axs[0,1].plot(tiempo,me(I3,S1S)[0], 'g')
axs[0,1].plot(tiempo,me(I3,S2S)[0], 'b')
axs[1,0].plot(tiempo,me(I3,S0C)[1], 'r')
axs[1,0].plot(tiempo,me(I3,S1C)[1], 'g')
axs[1,0].plot(tiempo,me(I3,S2C)[1], 'b')
axs[1,1].plot(tiempo,me(I3,S0C)[0], 'r')
axs[1,1].plot(tiempo,me(I3,S1C)[0], 'g')
axs[1,1].plot(tiempo,me(I3,S2C)[0], 'b')
rcParams.update({'font.size': 6})
savefig('logi01.png')


#Graficar
fig, axs = subplots(2,2)
axs[0,0].plot(tiempo,me(I4,S0S)[1], 'r')
axs[0,0].plot(tiempo,me(I4,S1S)[1], 'g')
axs[0,0].plot(tiempo,me(I4,S2S)[1], 'b')
axs[0,1].plot(tiempo,me(I4,S0S)[0], 'r')
axs[0,1].plot(tiempo,me(I4,S1S)[0], 'g')
axs[0,1].plot(tiempo,me(I4,S2S)[0], 'b')
axs[1,0].plot(tiempo,me(I4,S0C)[1], 'r')
axs[1,0].plot(tiempo,me(I4,S1C)[1], 'g')
axs[1,0].plot(tiempo,me(I4,S2C)[1], 'b')
axs[1,1].plot(tiempo,me(I4,S0C)[0], 'r')
axs[1,1].plot(tiempo,me(I4,S1C)[0], 'g')
axs[1,1].plot(tiempo,me(I4,S2C)[0], 'b')
rcParams.update({'font.size': 6})
savefig('logi11.png')


#Graficar
fig, axs = subplots(2,2)
axs[0,0].plot(tiempo,me(I5,S0S)[1], 'r')
axs[0,0].plot(tiempo,me(I5,S1S)[1], 'g')
axs[0,0].plot(tiempo,me(I5,S2S)[1], 'b')
axs[0,1].plot(tiempo,me(I5,S0S)[0], 'r')
axs[0,1].plot(tiempo,me(I5,S1S)[0], 'g')
axs[0,1].plot(tiempo,me(I5,S2S)[0], 'b')
axs[1,0].plot(tiempo,me(I5,S0C)[1], 'r')
axs[1,0].plot(tiempo,me(I5,S1C)[1], 'g')
axs[1,0].plot(tiempo,me(I5,S2C)[1], 'b')
axs[1,1].plot(tiempo,me(I5,S0C)[0], 'r')
axs[1,1].plot(tiempo,me(I5,S1C)[0], 'g')
axs[1,1].plot(tiempo,me(I5,S2C)[0], 'b')
rcParams.update({'font.size': 6})
savefig('logi00.png')





