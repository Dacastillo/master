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
S0S = [sigmen1,sigmen2]
S1S = [np.sqrt(1.1)*sigmen1,np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1,np.sqrt(0.1)*sigmas2]
S2S = [np.sqrt(1.1)*sigmen1+np.sqrt(1.1)*sigmas1,np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]
S0C = [sigmen1+sigmen2]
S1C = [np.sqrt(1.1)*sigmen1+np.sqrt(1.1)*sigmen2,np.sqrt(0.1)*sigmas1+np.sqrt(0.1)*sigmas2]
S2C = [np.sqrt(1.1)*sigmen1+np.sqrt(0.1)*sigmas1+np.sqrt(1.1)*sigmen2+np.sqrt(0.1)*sigmas2]
#Definir funcion logaritmo segura

def log_2(x):
    if x <= 0:
       return 0
    return np.log2(x)
#Definir funcion que calcula ecuaciones maestras y evaluar si funciona fuera
def me3(IN,RES):
    sol=mesolve(tensor(identity(2),identity(2)), IN, times, RES)
    out=[[0 for i in range(100)],[0 for i in range(100)]]
    conc=[0 for i in range(100)]
    mutu=[0 for i in range(100)]
    for i in range (0,100):
        mat=Qobj(sol.states[i])
        conc[i]=round(concurrence(mat),4)
        mutu[i]=round(entropy_mutual(mat,0,1)-entropy_conditional(mat,0),4)
    out=[conc,mutu]
    return out

def me2(IN,RES):
    sol=mesolve(tensor(identity(2),identity(2)), IN, times, RES)
    out=[[0 for i in range(100)],[0 for i in range(100)]]
    conc=[0 for i in range(100)]
    disc=[0 for i in range(100)]
    for i in range (0,100):
        mat=Qobj(sol.states[i])
        c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
        c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
        c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
        consar=np.array([c1,c2,c3])
        c=np.amax(consar)       
        conc[i]=round(concurrence(mat), 4)
        disc[i]=-0.5*((1+c)*log_2(1+c)+(1-c)*log_2(1-c))
        for j in range (0,4):
            disc[i]=disc[i]+mat.eigenenergies()[j]*log_2(4*mat.eigenenergies()[j])
    out=[conc,disc]
    return out    

tiempo = [(1/20)*i for i in range(100)]#Intervalo de tiempo para los gráficos
print(me2(I1,S0S)[1])
 
#Graficar
fig, axs = subplots(2,2)
axs[0,0].plot(tiempo,me2(I1,S0S)[1])
axs[0,0].plot(tiempo,me2(I1,S1S)[1])
axs[0,0].plot(tiempo,me2(I1,S2S)[1])
axs[0,0].set_title('Discordia sin acoplamiento')
axs[0,1].plot(tiempo,me2(I1,S0S)[0])
axs[0,1].plot(tiempo,me2(I1,S1S)[0])
axs[0,1].plot(tiempo,me2(I1,S2S)[0])
axs[0,1].set_title('Concurrencia sin acoplamiento')
axs[1,0].plot(tiempo,me2(I1,S0C)[1])
axs[1,0].plot(tiempo,me2(I1,S1C)[1])
axs[1,0].plot(tiempo,me2(I1,S2C)[1])
axs[1,0].set_title('Discordia con acoplamiento')
axs[1,1].plot(tiempo,me2(I1,S0C)[0])
axs[1,1].plot(tiempo,me2(I1,S1C)[0])
axs[1,1].plot(tiempo,me2(I1,S2C)[0])
axs[1,1].set_title('Concurrencia con acoplamiento')
for ax in fig.get_axes():
    ax.label_outer()
savefig('bell1.png')


