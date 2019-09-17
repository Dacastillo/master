#for i in range (1,20):
#    print(entropy_vn(result1.states[10*i]), entropy_vn(result2.states[10*i]), entropy_vn(result3.states[10*i]))
#figure()
#plot(times, result.expect[0])
#plot(times, result.expect[1])
#xlabel('Gamma*Tiempo')
#ylabel('Quantum Discord')
#ylabel('Concurrencia')
#legend(('Reservorio Vacio', 'Reservorio Termico', 'Reservorio Comprimido))
#show()
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
S0Sin = Qobj( np.array( [ [0.0, 0.0], [1.0, 0.0] ] ) )#Reservorio vacio sin interaccion con el otro 
S1Sin = Qobj( np.array( [ [0.0, 0.0], [1.1, 0.0] ] ) )#Reservorio termal sin interaccion con el otro 
S2Sin = Qobj( np.array( [ [0.0, -0.1], [1.1, 0.0] ] ) )#Reservorio comprimido sin interaccion con el otro 
S0Cin = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 1.0, 0.0] ]) ) #Reservorios vacios con interaccion
S1Cin = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [0.0, 1.1, 1.1, 0.0] ]) ) #Reservorios termales con interaccion
S2Cin = Qobj( np.array( [ [0.0,-0.1,-0.1, 0.0], [1.1, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [0.0, 1.1, 1.1, 0.0] ]) ) #Reservorios comprimidos con interaccion 
em_I1_S0Cin = mesolve( identity(4), I1, times, S0Cin )  #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios con interaccion
em_I2_S0Cin = mesolve( identity(4), I2, times, S0Cin )  #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios con interaccion
em_I3_S0Cin = mesolve( identity(4), I3, times, S0Cin )  #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios con interaccion
em_I4_S0Cin = mesolve( identity(4), I4, times, S0Cin )  #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios con interaccion 
em_I5_S0Cin = mesolve( identity(4), I5, times, S0Cin )  #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios con interaccion
em_I1_S1Cin = mesolve( identity(4), I1, times, S1Cin )  #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales con tinteraccion
em_I2_S1Cin = mesolve( identity(4), I2, times, S1Cin ) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales con interaccion
em_I3_S1Cin = mesolve( identity(4), I3, times, S1Cin ) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales con interaccion
em_I4_S1Cin = mesolve( identity(4), I4, times, S1Cin ) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales con interaccion
em_I5_S1Cin = mesolve( identity(4), I5, times, S1Cin ) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales con interaccion
em_I1_S2Cin = mesolve( identity(4), I1, times, S2Cin ) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos con interaccion
em_I2_S2Cin = mesolve( identity(4), I2, times, S2Cin ) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos con interaccion
em_I3_S2Cin = mesolve( identity(4), I3, times, S2Cin ) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos con interaccion
em_I4_S2Cin = mesolve( identity(4), I4, times, S2Cin ) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos con interaccion
em_I5_S2Cin = mesolve( identity(4), I5, times, S2Cin ) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos con interaccion
emA_I1_S0Sin = mesolve( identity(2), I1_A, times) #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios sin interaccion
emA_I2_S0Sin = mesolve( identity(2), I2_A, times) #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios sin interaccion
emA_I3_S0Sin = mesolve( identity(2), I3_A, times) #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios sin interaccion
emA_I4_S0Sin = mesolve( identity(2), I4_A, times) #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios sin interaccion
emA_I5_S0Sin = mesolve( identity(2), I5_A, times) #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios sin interaccion
emA_I1_S1Sin = mesolve( identity(2), I1_A, times) #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales sin interaccion
emA_I2_S1Sin = mesolve( identity(2), I2_A, times) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales sin interaccion
emA_I3_S1Sin = mesolve( identity(2), I3_A, times) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales sin interaccion
emA_I4_S1Sin = mesolve( identity(2), I4_A, times) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales sin interaccion
emA_I5_S1Sin = mesolve( identity(2), I5_A, times) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales sin interaccion
emA_I1_S2Sin = mesolve( identity(2), I1_A, times) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos sin interaccion 
emA_I2_S2Sin = mesolve( identity(2), I2_A, times) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos sin interaccion
emA_I3_S2Sin = mesolve( identity(2), I3_A, times) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos sin interaccion
emA_I4_S2Sin = mesolve( identity(2), I4_A, times) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos sin interaccion
emA_I5_S2Sin = mesolve( identity(2), I5_A, times) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos sin interaccion
emB_I1_S0Sin = mesolve( identity(2), I1_B, times) #Ecuacion Maestra para estado inicial Bell 00  
emB_I2_S0Sin = mesolve( identity(2), I2_B, times) #Ecuacion Maestra para estado inicial Bell 10
emB_I3_S0Sin = mesolve( identity(2), I3_B, times) #Ecuacion Maestra para estado inicial logico 01
emB_I4_S0Sin = mesolve( identity(2), I4_B, times) #Ecuacion Maestra para estado inicial logico 11
emB_I5_S0Sin = mesolve( identity(2), I5_B, times) #Ecuacion Maestra para estado inicial logico 00
emB_I1_S1Sin = mesolve( identity(2), I1_B, times) #Ecuacion Maestra para estado inicial Bell 00
emB_I2_S1Sin = mesolve( identity(2), I2_B, times) #Ecuacion Maestra para estado inicial Bell 10
emB_I3_S1Sin = mesolve( identity(2), I3_B, times) #Ecuacion Maestra para estado inicial logico 01 
emB_I4_S1Sin = mesolve( identity(2), I4_B, times) #Ecuacion Maestra para estado inicial logico 11
emB_I5_S1Sin = mesolve( identity(2), I5_B, times) #Ecuacion Maestra para estado inicial logico 00
emB_I1_S2Sin = mesolve( identity(2), I1_B, times) #Ecuacion Maestra para estado inicial Bell 00
emB_I2_S2Sin = mesolve( identity(2), I2_B, times) #Ecuacion Maestra para estado inicial Bell 10
emB_I3_S2Sin = mesolve( identity(2), I3_B, times) #Ecuacion Maestra para estado inicial logico 01
emB_I4_S2Sin = mesolve( identity(2), I4_B, times) #Ecuacion Maestra para estado inicial logico 11
emB_I5_S2Sin = mesolve( identity(2), I5_B, times) #Ecuacion Maestra para estado inicial logico 00

