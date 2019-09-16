from qutip import *
from matplotlib.pyplot import *
import numpy as np
H = np.sqrt(1.1) * sigmap() - np.sqrt(0.1) * sigmam()
est0=qeye(2)
est1=projection(2,0,0)
est2=projection(2,1,1)
times = np.linspace(int(0.0), int(10.0), int(60.0))
result1 = mesolve(H, est0, times)
result2 = mesolve(H, est1, times)
result3 = mesolve(H, est2, times)
fin0 = result1.states[2]
fin1 = result2.states[2]
fin2 = result3.states[2]
eig1 = fin0.eigenstates[0]
#figure()
#plot(times, result.expect[0])
#plot(times, result.expect[1])
#xlabel('Tiempo')
#ylabel('Valores de Expectacion')
#legend(('numero de fotones en cavidad', 'probabilidad de excitacion atomica'))
#show()
