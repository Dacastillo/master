from qutip import * #Liberia qutip
from matplotlib.pyplot import * #Libreria matplotlib
import numpy as np #Liberia numpy
I1 = Qobj( np.array( [ [0.5, 0.0, 0.0, 0.5], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.5, 0.0, 0.0, 0.5] ] ) ) #Definir estado inicial Bell 1
I1_A = Qobj( np.array( [[0.5, 0.0], [0.0, 0.5]] ) ) #Traza parcial A
I1_B = Qobj( np.array( [[0.5, 0.0], [0.0, 0.5]] ) ) #Traza parcial B
I2 = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0], [0.0, 0.5, 0.5, 0.0], [0.0, 0.0, 0.0, 0.0] ] ) ) #Definir estado inicial Bell 3
I2_A = Qobj( np.array( [[0.5, 0.0], [0.0, 0.5]] ) ) #Traza parcial A
I2_B = Qobj( np.array( [[0.5, 0.0], [0.0, 0.5]] ) ) #Traza parcial B
I3 = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0] ] ) ) #Definir estado inicial logico 01
I3_A = Qobj( np.array( [[1.0, 0.0], [0.0, 0.0]] ) ) #Traza parcial A
I3_B = Qobj( np.array( [[0.0, 0.0], [0.0, 1.0]] ) ) #Traza parcial B
I4 = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0] ] ) ) #Definir estado inicial logico 11
I4_A = Qobj( np.array( [[0.0, 0.0], [0.0, 1.0]] ) )#Traza parcoial A
I4_B = Qobj( np.array( [[0.0, 0.0], [0.0, 1.0]] ) )#Traza parcial B
I5 = Qobj( np.array( [ [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0] ] ) ) #Definir estado inicial logico 00
I5_A = Qobj( np.array( [[1.0, 0.0], [0.0, 0.0]] ) )#Traza parcial A
I5_B = Qobj( np.array( [[1.0, 0.0], [0.0, 0.0]] ) )#Traza parcial B
times = np.linspace(int(0.0), int(10.0), int(1000.0)) #Definir intervalo temporal
S0S = Qobj( np.array( [ [0.0, 0.0], [1.0, 0.0] ] ) )#Reservorio vacio sin interaccion con el otro 
S1S = Qobj( np.array( [ [0.0, 0.0], [1.1, 0.0] ] ) )#Reservorio termal sin interaccion con el otro 
S2S = Qobj( np.array( [ [0.0, -0.1], [1.1, 0.0] ] ) )#Reservorio comprimido sin interaccion con el otro 
S0C = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 1.0, 0.0] ]) ) #Reservorios vacios con interaccion
S1C = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [0.0, 1.1, 1.1, 0.0] ]) ) #Reservorios termales con interaccion
S2C = Qobj( np.array( [ [0.0,-0.1,-0.1, 0.0], [1.1, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [0.0, 1.1, 1.1, 0.0] ]) ) #Reservorios comprimidos con interaccion 
em_I1_S0C = mesolve(identity(4), I1, times, S0C)  #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios con interaccion
em_I2_S0C = mesolve(identity(4), I2, times, S0C)  #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios con interaccion
em_I3_S0C = mesolve(identity(4), I3, times, S0C)  #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios con interaccion
em_I4_S0C = mesolve(identity(4), I4, times, S0C)  #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios con interaccion 
em_I5_S0C = mesolve(identity(4), I5, times, S0C)  #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios con interaccion
em_I1_S1C = mesolve(identity(4), I1, times, S1C)  #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales con tinteraccion
em_I2_S1C = mesolve(identity(4), I2, times, S1C) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales con interaccion
em_I3_S1C = mesolve(identity(4), I3, times, S1C) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales con interaccion
em_I4_S1C = mesolve(identity(4), I4, times, S1C) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales con interaccion
em_I5_S1C = mesolve(identity(4), I5, times, S1C) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales con interaccion
em_I1_S2C = mesolve(identity(4), I1, times, S2C) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos con interaccion
em_I2_S2C = mesolve(identity(4), I2, times, S2C) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos con interaccion
em_I3_S2C = mesolve(identity(4), I3, times, S2C) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos con interaccion
em_I4_S2C = mesolve(identity(4), I4, times, S2C) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos con interaccion
em_I5_S2C = mesolve(identity(4), I5, times, S2C) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos con interaccion
emA_I1_S0S = mesolve(identity(2), I1_A, times, S0S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios sin interaccion
emA_I2_S0S = mesolve(identity(2), I2_A, times, S0S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios sin interaccion
emA_I3_S0S = mesolve(identity(2), I3_A, times, S0S) #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios sin interaccion
emA_I4_S0S = mesolve(identity(2), I4_A, times, S0S) #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios sin interaccion
emA_I5_S0S = mesolve(identity(2), I5_A, times, S0S) #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios sin interaccion
emA_I1_S1S = mesolve(identity(2), I1_A, times, S1S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales sin interaccion
emA_I2_S1S = mesolve(identity(2), I2_A, times, S1S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales sin interaccion
emA_I3_S1S = mesolve(identity(2), I3_A, times, S1S) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales sin interaccion
emA_I4_S1S = mesolve(identity(2), I4_A, times, S1S) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales sin interaccion
emA_I5_S1S = mesolve(identity(2), I5_A, times, S1S) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales sin interaccion
emA_I1_S2S = mesolve(identity(2), I1_A, times, S2S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos sin interaccion 
emA_I2_S2S = mesolve(identity(2), I2_A, times, S2S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos sin interaccion
emA_I3_S2S = mesolve(identity(2), I3_A, times, S2S) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos sin interaccion
emA_I4_S2S = mesolve(identity(2), I4_A, times, S2S) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos sin interaccion
emA_I5_S2S = mesolve(identity(2), I5_A, times, S2S) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos sin interaccion
emB_I1_S0S = mesolve(identity(2), I1_B, times, S0S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios sin interaccion 
emB_I2_S0S = mesolve(identity(2), I2_B, times, S0S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios sin interaccion
emB_I3_S0S = mesolve(identity(2), I3_B, times, S0S) #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios sin interaccion
emB_I4_S0S = mesolve(identity(2), I4_B, times, S0S) #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios sin interaccion
emB_I5_S0S = mesolve(identity(2), I5_B, times, S0S) #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios sin interaccion
emB_I1_S1S = mesolve(identity(2), I1_B, times, S1S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales sin interaccion
emB_I2_S1S = mesolve(identity(2), I2_B, times, S1S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales sin interaccion 
emB_I3_S1S = mesolve(identity(2), I3_B, times, S1S) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales sin interaccion
emB_I4_S1S = mesolve(identity(2), I4_B, times, S1S) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales sin interaccion
emB_I5_S1S = mesolve(identity(2), I5_B, times, S1S) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales sin interaccion 
emB_I1_S2S = mesolve(identity(2), I1_B, times, S2S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos sin interaccion
emB_I2_S2S = mesolve(identity(2), I2_B, times, S2S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos sin interaccion 
emB_I3_S2S = mesolve(identity(2), I3_B, times, S2S) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos sin interaccion
emB_I4_S2S = mesolve(identity(2), I4_B, times, S2S) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos sin interaccion
emB_I5_S2S = mesolve(identity(2), I5_B, times, S2S) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos sin interaccion

     
n = 10
#Calcular todos los discord (mutua-A-condicional) y las concurrencias necesarias
tiempo = [0.01*i for i in range(n)]
#conc_I1_S0C = [0 for i in range(n)]
#disc_I1_S0C = [0 for i in range(n)]
#conc_I2_S0C = [0 for i in range(n)]
#disc_I2_S0C = [0 for i in range(n)]
#conc_I3_S0C = [0 for i in range(n)]
#disc_I3_S0C = [0 for i in range(n)]
#conc_I4_S0C = [0 for i in range(n)]
#disc_I4_S0C = [0 for i in range(n)]
#conc_I5_S0C = [0 for i in range(n)]
#disc_I5_S0C = [0 for i in range(n)]
#conc_I1_S1C = [0 for i in range(n)]
#disc_I1_S1C = [0 for i in range(n)]
#conc_I2_S1C = [0 for i in range(n)]
#disc_I2_S1C = [0 for i in range(n)]
#conc_I3_S1C = [0 for i in range(n)]
#disc_I3_S1C = [0 for i in range(n)]
#conc_I4_S1C = [0 for i in range(n)]
#disc_I4_S1C = [0 for i in range(n)]
#conc_I5_S1C = [0 for i in range(n)]
#disc_I5_S1C = [0 for i in range(n)]
#conc_I1_S2C = [0 for i in range(n)]
#disc_I1_S2C = [0 for i in range(n)]
#conc_I2_S2C = [0 for i in range(n)]
#disc_I2_S2C = [0 for i in range(n)]
#conc_I3_S2C = [0 for i in range(n)]
#disc_I3_S2C = [0 for i in range(n)]
#conc_I4_S2C = [0 for i in range(n)]
#disc_I4_S2C = [0 for i in range(n)]
#conc_I5_S2C = [0 for i in range(n)]
#disc_I5_S2C = [0 for i in range(n)]
#conc_I1_S0S = [0 for i in range(n)]
#disc_I1_S0S = [0 for i in range(n)]
#conc_I2_S0S = [0 for i in range(n)]
#disc_I2_S0S = [0 for i in range(n)]
#conc_I3_S0S = [0 for i in range(n)]
#disc_I3_S0S = [0 for i in range(n)]
#conc_I4_S0S = [0 for i in range(n)]
#disc_I4_S0S = [0 for i in range(n)]
#conc_I5_S0S = [0 for i in range(n)]
#disc_I5_S0S = [0 for i in range(n)]
#conc_I1_S1S = [0 for i in range(n)]
#disc_I1_S1S = [0 for i in range(n)]
#conc_I2_S1S = [0 for i in range(n)]
#disc_I2_S1S = [0 for i in range(n)]
#conc_I3_S1S = [0 for i in range(n)]
#disc_I3_S1S = [0 for i in range(n)]
#conc_I4_S1S = [0 for i in range(n)]
#disc_I4_S1S = [0 for i in range(n)]
#conc_I5_S1S = [0 for i in range(n)]
#disc_I5_S1S = [0 for i in range(n)]
#conc_I1_S2S = [0 for i in range(n)]
#disc_I1_S2S = [0 for i in range(n)]
#conc_I2_S2S = [0 for i in range(n)]
#disc_I2_S2S = [0 for i in range(n)]
#conc_I3_S2S = [0 for i in range(n)]
#disc_I3_S2S = [0 for i in range(n)]
#conc_I4_S2S = [0 for i in range(n)]
#disc_I4_S2S = [0 for i in range(n)]
#conc_I5_S2S = [0 for i in range(n)]
#disc_I5_S2S = [0 for i in range(n)]
for var in ['disc', 'conc']:
    for est in ['I1_A', 'I2_A', 'I3_A', 'I4_A', 'I5_A']:
        for res in ['S0S', 'S1S', 'S2S']:
            var_est_res= [0 for i in range(n)] 
#            print(var_est_res])
#for i in range (0,n):
#      conc_I1_S0S[i] = concurrence(Qobj(tensor(emA_I1_S0S.states[i],emB_I1_S0S.states[i])))
#      disc_I1_S0S[i] = entropy_mutual(Qobj(tensor(emA_I1_S0S.states[i],emB_I1_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I1_S0S.states[i],emB_I1_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I1_S0S.states[i],emB_I1_S0S.states[i])).ptrace(0))
#      conc_I2_S0S[i] = concurrence(Qobj(tensor(emA_I2_S0S.states[i],emB_I2_S0S.states[i])))
#      disc_I2_S0S[i] = entropy_mutual(Qobj(tensor(emA_I2_S0S.states[i],emB_I2_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I2_S0S.states[i],emB_I2_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I2_S0S.states[i],emB_I2_S0S.states[i])).ptrace(0))
#      conc_I3_S0S[i] = concurrence(Qobj(tensor(emA_I3_S0S.states[i],emB_I3_S0S.states[i])))
#      disc_I3_S0S[i] = entropy_mutual(Qobj(tensor(emA_I3_S0S.states[i],emB_I3_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I3_S0S.states[i],emB_I3_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I3_S0S.states[i],emB_I3_S0S.states[i])).ptrace(0))
#      conc_I4_S0S[i] = concurrence(Qobj(tensor(emA_I4_S0S.states[i],emB_I4_S0S.states[i])))
#      disc_I4_S0S[i] = entropy_mutual(Qobj(tensor(emA_I4_S0S.states[i],emB_I4_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I4_S0S.states[i],emB_I4_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I4_S0S.states[i],emB_I1_S0S.states[i])).ptrace(0))
#      conc_I5_S0S[i] = concurrence(Qobj(tensor(emA_I5_S0S.states[i],emB_I5_S0S.states[i])))
#      disc_I5_S0S[i] = entropy_mutual(Qobj(tensor(emA_I5_S0S.states[i],emB_I5_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I5_S0S.states[i],emB_I5_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I5_S0S.states[i],emB_I1_S0S.states[i])).ptrace(0))
#      conc_I1_S1S[i] = concurrence(Qobj(tensor(emA_I1_S1S.states[i],emB_I1_S1S.states[i])))
#      disc_I1_S1S[i] = entropy_mutual(Qobj(tensor(emA_I1_S1S.states[i],emB_I1_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I1_S1S.states[i],emB_I1_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I1_S1S.states[i],emB_I1_S1S.states[i])).ptrace(0))
#      conc_I2_S1S[i] = concurrence(Qobj(tensor(emA_I2_S1S.states[i],emB_I2_S1S.states[i])))
#      disc_I2_S1S[i] = entropy_mutual(Qobj(tensor(emA_I2_S1S.states[i],emB_I2_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I2_S1S.states[i],emB_I2_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I2_S1S.states[i],emB_I2_S1S.states[i])).ptrace(0))
#      conc_I3_S1S[i] = concurrence(Qobj(tensor(emA_I3_S1S.states[i],emB_I3_S1S.states[i])))
#      disc_I3_S1S[i] = entropy_mutual(Qobj(tensor(emA_I3_S1S.states[i],emB_I3_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I3_S1S.states[i],emB_I3_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I3_S1S.states[i],emB_I3_S1S.states[i])).ptrace(0))
#      conc_I4_S1S[i] = concurrence(Qobj(tensor(emA_I4_S1S.states[i],emB_I4_S1S.states[i])))
#      disc_I4_S1S[i] = entropy_mutual(Qobj(tensor(emA_I4_S1S.states[i],emB_I4_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I4_S1S.states[i],emB_I4_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I4_S1S.states[i],emB_I4_S1S.states[i])).ptrace(0))
#      conc_I5_S1S[i] = concurrence(Qobj(tensor(emA_I5_S1S.states[i],emB_I5_S1S.states[i])))
#      disc_I5_S1S[i] = entropy_mutual(Qobj(tensor(emA_I5_S1S.states[i],emB_I5_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I5_S1S.states[i],emB_I5_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I5_S1S.states[i],emB_I5_S1S.states[i])).ptrace(0))
#      conc_I1_S2S[i] = concurrence(Qobj(tensor(emA_I1_S2S.states[i],emB_I1_S2S.states[i])))
#      disc_I1_S2S[i] = entropy_mutual(Qobj(tensor(emA_I1_S2S.states[i],emB_I1_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I1_S2S.states[i],emB_I1_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I1_S2S.states[i],emB_I1_S2S.states[i])).ptrace(0))
#      conc_I2_S2S[i] = concurrence(Qobj(tensor(emA_I2_S2S.states[i],emB_I2_S2S.states[i])))
#      disc_I2_S2S[i] = entropy_mutual(Qobj(tensor(emA_I2_S2S.states[i],emB_I2_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I2_S2S.states[i],emB_I2_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I2_S2S.states[i],emB_I2_S2S.states[i])).ptrace(0))
#      conc_I3_S2S[i] = concurrence(Qobj(tensor(emA_I3_S2S.states[i],emB_I3_S2S.states[i])))
#      disc_I3_S2S[i] = entropy_mutual(Qobj(tensor(emA_I3_S2S.states[i],emB_I3_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I3_S2S.states[i],emB_I3_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I3_S2S.states[i],emB_I3_S2S.states[i])).ptrace(0))
#      conc_I4_S2S[i] = concurrence(Qobj(tensor(emA_I4_S2S.states[i],emB_I4_S2S.states[i])))
#      disc_I4_S2S[i] = entropy_mutual(Qobj(tensor(emA_I4_S2S.states[i],emB_I4_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I4_S2S.states[i],emB_I4_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I4_S2S.states[i],emB_I4_S2S.states[i])).ptrace(0))
#      conc_I5_S2S[i] = concurrence(Qobj(tensor(emA_I5_S2S.states[i],emB_I5_S2S.states[i])))
#      disc_I5_S2S[i] = entropy_mutual(Qobj(tensor(emA_I5_S2S.states[i],emB_I5_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I5_S2S.states[i],emB_I5_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I5_S2S.states[i],emB_I5_S2S.states[i])).ptrace(0))
#      conc_I1_S0S[i] = concurrence(Qobj(tensor(emA_I1_S0S.states[i],emB_I1_S0S.states[i])))
#      disc_I1_S0S[i] = entropy_mutual(Qobj(tensor(emA_I1_S0S.states[i],emB_I1_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I1_S0S.states[i],emB_I1_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I1_S0S.states[i],emB_I1_S0S.states[i])).ptrace(0))
#      conc_I2_S0S[i] = concurrence(Qobj(tensor(emA_I2_S0S.states[i],emB_I2_S0S.states[i])))
#      disc_I2_S0S[i] = entropy_mutual(Qobj(tensor(emA_I2_S0S.states[i],emB_I2_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I2_S0S.states[i],emB_I2_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I2_S0S.states[i],emB_I2_S0S.states[i])).ptrace(0))
#      conc_I3_S0S[i] = concurrence(Qobj(tensor(emA_I3_S0S.states[i],emB_I3_S0S.states[i])))
#      disc_I3_S0S[i] = entropy_mutual(Qobj(tensor(emA_I3_S0S.states[i],emB_I3_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I3_S0S.states[i],emB_I3_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I3_S0S.states[i],emB_I3_S0S.states[i])).ptrace(0))
#      conc_I4_S0S[i] = concurrence(Qobj(tensor(emA_I4_S0S.states[i],emB_I4_S0S.states[i])))
#      disc_I4_S0S[i] = entropy_mutual(Qobj(tensor(emA_I4_S0S.states[i],emB_I4_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I4_S0S.states[i],emB_I4_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I4_S0S.states[i],emB_I1_S0S.states[i])).ptrace(0))
#      conc_I5_S0S[i] = concurrence(Qobj(tensor(emA_I5_S0S.states[i],emB_I5_S0S.states[i])))
#      disc_I5_S0S[i] = entropy_mutual(Qobj(tensor(emA_I5_S0S.states[i],emB_I5_S0S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I5_S0S.states[i],emB_I5_S0S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I5_S0S.states[i],emB_I1_S0S.states[i])).ptrace(0))
#      conc_I1_S1S[i] = concurrence(Qobj(tensor(emA_I1_S1S.states[i],emB_I1_S1S.states[i])))
#      disc_I1_S1S[i] = entropy_mutual(Qobj(tensor(emA_I1_S1S.states[i],emB_I1_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I1_S1S.states[i],emB_I1_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I1_S1S.states[i],emB_I1_S1S.states[i])).ptrace(0))
#      conc_I2_S1S[i] = concurrence(Qobj(tensor(emA_I2_S1S.states[i],emB_I2_S1S.states[i])))
#      disc_I2_S1S[i] = entropy_mutual(Qobj(tensor(emA_I2_S1S.states[i],emB_I2_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I2_S1S.states[i],emB_I2_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I2_S1S.states[i],emB_I2_S1S.states[i])).ptrace(0))
#      conc_I3_S1S[i] = concurrence(Qobj(tensor(emA_I3_S1S.states[i],emB_I3_S1S.states[i])))
#      disc_I3_S1S[i] = entropy_mutual(Qobj(tensor(emA_I3_S1S.states[i],emB_I3_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I3_S1S.states[i],emB_I3_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I3_S1S.states[i],emB_I3_S1S.states[i])).ptrace(0))
#      conc_I4_S1S[i] = concurrence(Qobj(tensor(emA_I4_S1S.states[i],emB_I4_S1S.states[i])))
#      disc_I4_S1S[i] = entropy_mutual(Qobj(tensor(emA_I4_S1S.states[i],emB_I4_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I4_S1S.states[i],emB_I4_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I4_S1S.states[i],emB_I4_S1S.states[i])).ptrace(0))
#      conc_I5_S1S[i] = concurrence(Qobj(tensor(emA_I5_S1S.states[i],emB_I5_S1S.states[i])))
#      disc_I5_S1S[i] = entropy_mutual(Qobj(tensor(emA_I5_S1S.states[i],emB_I5_S1S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I5_S1S.states[i],emB_I5_S1S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I5_S1S.states[i],emB_I5_S1S.states[i])).ptrace(0))
#      conc_I1_S2S[i] = concurrence(Qobj(tensor(emA_I1_S2S.states[i],emB_I1_S2S.states[i])))
#      disc_I1_S2S[i] = entropy_mutual(Qobj(tensor(emA_I1_S2S.states[i],emB_I1_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I1_S2S.states[i],emB_I1_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I1_S2S.states[i],emB_I1_S2S.states[i])).ptrace(0))
#      conc_I2_S2S[i] = concurrence(Qobj(tensor(emA_I2_S2S.states[i],emB_I2_S2S.states[i])))
#      disc_I2_S2S[i] = entropy_mutual(Qobj(tensor(emA_I2_S2S.states[i],emB_I2_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I2_S2S.states[i],emB_I2_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I2_S2S.states[i],emB_I2_S2S.states[i])).ptrace(0))
#      conc_I3_S2S[i] = concurrence(Qobj(tensor(emA_I3_S2S.states[i],emB_I3_S2S.states[i])))
#      disc_I3_S2S[i] = entropy_mutual(Qobj(tensor(emA_I3_S2S.states[i],emB_I3_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I3_S2S.states[i],emB_I3_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I3_S2S.states[i],emB_I3_S2S.states[i])).ptrace(0))
#      conc_I4_S2S[i] = concurrence(Qobj(tensor(emA_I4_S2S.states[i],emB_I4_S2S.states[i])))
#      disc_I4_S2S[i] = entropy_mutual(Qobj(tensor(emA_I4_S2S.states[i],emB_I4_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I4_S2S.states[i],emB_I4_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I4_S2S.states[i],emB_I4_S2S.states[i])).ptrace(0))
#      conc_I5_S2S[i] = concurrence(Qobj(tensor(emA_I5_S2S.states[i],emB_I5_S2S.states[i])))
#      disc_I5_S2S[i] = entropy_mutual(Qobj(tensor(emA_I5_S2S.states[i],emB_I5_S2S.states[i])),0,1)+entropy_conditional(Qobj(tensor(emA_I5_S2S.states[i],emB_I5_S2S.states[i])),1)-entropy_vn(Qobj(tensor(emA_I5_S2S.states[i],emB_I5_S2S.states[i])).ptrace(0))

#Graficar
#figure()
#plot(tiempo,disc_I1_S0S)
#plot(tiempo,disc_I1_S1S)
#plot(tiempo,disc_I1_S2S)
#xlabel('gamma tiempo')
#ylabel('discordia cuantica')
#legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell1_S.png')

#figure()
#plot(tiempo,disc_I2_S0S)
#plot(tiempo,disc_I2_S1S)
#plot(tiempo,disc_I2_S2S)
#xlabel('gamma tiempo')
#ylabel('discordia cuantica')
#legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
#savefig('disc_bell3_S.png')

#figure()
#plot(tiempo,disc_I3_S0S)
#plot(tiempo,disc_I3_S1S)
#plot(tiempo,disc_I3_S2S)
#xlabel('gamma tiempo')
#ylabel('discordia cuantica')
#legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
#savefig('disc_logi2_S.png')

#figure()
#plot(tiempo,disc_I4_S0S)
#plot(tiempo,disc_I4_S1S)
#plot(tiempo,disc_I4_S2S)
#xlabel('gamma tiempo')
#ylabel('discordia cuantica')
#legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
#savefig('disc_logi4_S.png')

#figure()
#plot(tiempo,disc_I5_S0S)
#plot(tiempo,disc_I5_S1S)
#plot(tiempo,disc_I5_S2S)
#xlabel('gamma tiempo')
#ylabel('discordia cuantica')
#legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
#savefig('disc_logi1_S.png')

#figure()
#plot(tiempo,conc_I1_S0S)
#plot(tiempo,conc_I1_S1S)
#plot(tiempo,conc_I1_S2S)
#xlabel('gamma tiempo')
#ylabel('concurrencia')
#legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
#savefig('conc_bell1_S.png')

#figure()
#plot(tiempo,conc_I2_S0S)
#plot(tiempo,conc_I2_S1S)
#plot(tiempo,conc_I2_S2S)
#xlabel('gamma tiempo')
#ylabel('concurrencia')
#legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
#savefig('conc_bell3_S.png')

#figure()
#plot(tiempo,conc_I3_S0S)
#plot(tiempo,conc_I3_S1S)
#plot(tiempo,conc_I3_S2S)
#xlabel('gamma tiempo')
#ylabel('concurrencia')
#legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
#savefig('conc_logi3_S.png')

#figure()
#plot(tiempo,conc_I4_S0S)
#plot(tiempo,conc_I4_S1S)
#plot(tiempo,conc_I4_S2S)
#xlabel('gamma tiempo')
#ylabel('concurrencia')
#legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
#savefig('conc_logi4_S.png')

#figure()
#plot(tiempo,conc_I5_S0S)
#plot(tiempo,conc_I5_S1S)
#plot(tiempo,conc_I5_S2S)
#xlabel('gamma tiempo')
#ylabel('discordia cuantica')
#legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
#savefig('conc_logi1_S.png')

#Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,0).dag(),basis(4,0))+Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,1).dag(),basis(4,1))
#Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,0).dag(),basis(4,2))+Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,1).dag(),basis(4,3)) 
#Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,2).dag(),basis(4,0))+Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,3).dag(),basis(4,1))
#Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,2).dag(),basis(4,2))+Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,3).dag(),basis(4,3)) 

#Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,0).dag(),basis(4,0))+Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,2).dag(),basis(4,2))
#Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,0).dag(),basis(4,1))+Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,2).dag(),basis(4,3))
#Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,1).dag(),basis(4,0))+Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,3).dag(),basis(4,2))
#Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,1).dag(),basis(4,1))+Qobj(em_I3_S0C.states[21]).matrix_element(basis(4,3).dag(),basis(4,3))


for i in range (0,20):
    matA=Qobj(emA_I3_S0S.states[i])
    matB=Qobj(emB_I3_S0S.states[i])

    if tensor(matA,matB).eigenenergies()[0] > tensor(matA, matB).eigenenergies()[1]:
       if tensor(matA, matB).eigenenergies()[0] > tensor(matA, matB).eigenenergies()[2]:
          if tensor(matA, matB).eigenenergies()[0] > tensor(matA, matB).eigenenergies()[3]:
             conc=tensor(matA, matB).eigenenergies()[0]-tensor(matA, matB).eigenenergies()[1]-tensor(matA, matB).eigenenergies()[2]-tensor(matA, matB).eigenenergies()[3]

    if tensor(matA,matB).eigenenergies()[1] > tensor(matA, matB).eigenenergies()[0]:
       if tensor(matA, matB).eigenenergies()[1] > tensor(matA, matB).eigenenergies()[2]:
          if tensor(matA, matB).eigenenergies()[1] > tensor(matA, matB).eigenenergies()[3]:
             conc=tensor(matA, matB).eigenenergies()[1]-tensor(matA, matB).eigenenergies()[0]-tensor(matA, matB).eigenenergies()[2]-tensor(matA, matB).eigenenergies()[3]

    if tensor(matA,matB).eigenenergies()[2] > tensor(matA, matB).eigenenergies()[1]:
       if tensor(matA, matB).eigenenergies()[2] > tensor(matA, matB).eigenenergies()[0]:
          if tensor(matA, matB).eigenenergies()[2] > tensor(matA, matB).eigenenergies()[3]:
             conc=tensor(matA, matB).eigenenergies()[2]-tensor(matA, matB).eigenenergies()[1]-tensor(matA, matB).eigenenergies()[0]-tensor(matA, matB).eigenenergies()[3]

    if tensor(matA,matB).eigenenergies()[3] > tensor(matA, matB).eigenenergies()[1]:
       if tensor(matA, matB).eigenenergies()[3] > tensor(matA, matB).eigenenergies()[2]:
          if tensor(matA, matB).eigenenergies()[3] > tensor(matA, matB).eigenenergies()[0]:
             conc=tensor(matA, matB).eigenenergies()[3]-tensor(matA, matB).eigenenergies()[1]-tensor(matA, matB).eigenenergies()[2]-tensor(matA, matB).eigenenergies()[0]

    disc=-entropy_mutual(tensor(matA,matB),0,1)-entropy_conditional(tensor(matA,matB),0)+entropy_vn(matA)
    print(conc,disc)


for i in range (0,20):
    matA=Qobj(np.array([[Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,0).dag(),basis(4,0))+Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,1).dag(),basis(4,1)),Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,0).dag(),basis(4,2))+Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,1).dag(),basis(4,3)) ],[Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,2).dag(),basis(4,0))+Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,3).dag(),basis(4,1)) ,Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,2).dag(),basis(4,2))+Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,3).dag(),basis(4,3))]]))
    matB=Qobj(np.array([[Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,0).dag(),basis(4,0))+Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,2).dag(),basis(4,2)),Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,0).dag(),basis(4,1))+Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,2).dag(),basis(4,3))],[Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,1).dag(),basis(4,0))+Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,3).dag(),basis(4,2)),Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,1).dag(),basis(4,1))+Qobj(em_I3_S0C.states[i]).matrix_element(basis(4,3).dag(),basis(4,3))]]))

    if tensor(matA,matB).eigenenergies()[0] > tensor(matA, matB).eigenenergies()[1]:
       if tensor(matA, matB).eigenenergies()[0] > tensor(matA, matB).eigenenergies()[2]:
          if tensor(matA, matB).eigenenergies()[0] > tensor(matA, matB).eigenenergies()[3]:
             conc=tensor(matA, matB).eigenenergies()[0]-tensor(matA, matB).eigenenergies()[1]-tensor(matA, matB).eigenenergies()[2]-tensor(matA, matB).eigenenergies()[3]

 
    if tensor(matA,matB).eigenenergies()[1] > tensor(matA, matB).eigenenergies()[0]:
       if tensor(matA, matB).eigenenergies()[1] > tensor(matA, matB).eigenenergies()[2]:
          if tensor(matA, matB).eigenenergies()[1] > tensor(matA, matB).eigenenergies()[3]:
             conc=tensor(matA, matB).eigenenergies()[1]-tensor(matA, matB).eigenenergies()[0]-tensor(matA, matB).eigenenergies()[2]-tensor(matA, matB).eigenenergies()[3]

    if tensor(matA,matB).eigenenergies()[2] > tensor(matA, matB).eigenenergies()[1]:
       if tensor(matA, matB).eigenenergies()[2] > tensor(matA, matB).eigenenergies()[0]:
          if tensor(matA, matB).eigenenergies()[2] > tensor(matA, matB).eigenenergies()[3]:
             conc=tensor(matA, matB).eigenenergies()[2]-tensor(matA, matB).eigenenergies()[1]-tensor(matA, matB).eigenenergies()[0]-tensor(matA, matB).eigenenergies()[3]

    if tensor(matA,matB).eigenenergies()[3] > tensor(matA, matB).eigenenergies()[1]:
       if tensor(matA, matB).eigenenergies()[3] > tensor(matA, matB).eigenenergies()[2]:
          if tensor(matA, matB).eigenenergies()[3] > tensor(matA, matB).eigenenergies()[0]:
             conc=tensor(matA, matB).eigenenergies()[3]-tensor(matA, matB).eigenenergies()[1]-tensor(matA, matB).eigenenergies()[2]-tensor(matA, matB).eigenenergies()[0]

    disc=-entropy_mutual(tensor(matA,matB),0,1)-entropy_conditional(tensor(matA,matB),0)+entropy_vn(matA)
    print(conc,disc)
