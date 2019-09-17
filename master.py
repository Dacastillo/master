from qutip import *
from matplotlib.pyplot import *
import numpy as np
S0A = sigmam() #reservorio vacio
S1A = np.sqrt(1.1) * sigmam() #reservorio termal
S2A = np.sqrt(1.1) * sigmam() - np.sqrt(0.1) * sigmap() #reservorio comprimido 
x = np.array([[0,0,0,0.1],[0,0,0.1,0],[0,0,0,0],[1.1,0,0,0]])
S0AB = Qobj(x)
#S0AB = tensor([sigmam(),qeye(2)])+tensor([qeye(2),sigmam()]) #reservorios vacios con interaccion
#S1AB =(np.sqrt(1.1)*tensor([sigmam(),qeye(2)]))+(np.sqrt(1.1)*tensor([qeye(2),sigmam()])) #reservorios termales con interaccion
#S2AB =(np.sqrt(1.1)*tensor([sigmam(),qeye(2)]))-(np.sqrt(0.1)*tensor([sigmap(),qeye(2)]))+(np.sqrt(1.1)*tensor([qeye(2),sigmam()]))-(np.sqrt(0.1)*tensor([qeye(2),sigmap()])) #reservorios comprimidos con interaccion
times = np.linspace(int(0.0), int(10.0), int(1000.0))
result1 = mesolve(qeye(2), qeye(2), times, S0A)
result2 = mesolve(qeye(2), projection(2,0,0), times, S1A)
result3 = mesolve(qeye(2), projection(2,1,1), times, S2A)
result4 = mesolve(qeye(4), ket2dm(basis(4,3)), times, S0AB)
for i in range (1,20):
    print(entropy_vn(result1.states[10*i]), entropy_vn(result2.states[10*i]), entropy_vn(result3.states[10*i]))
#print(c)
#figure()
#plot(times, result.expect[0])
#plot(times, result.expect[1])
#xlabel('Gamma*Tiempo')
#ylabel('Quantum Discord')
#ylabel('Concurrencia')
#legend(('Reservorio Vacio', 'Reservorio Termico', 'Reservorio Comprimido))
#show()
