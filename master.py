from qutip import *
from matplotlib.pyplot import *
import numpy as np
H0 = sigmap() #reservorio vacio
H2 = np.sqrt(1.1) * sigmap() #reservorio termal
H2 = np.sqrt(1.1) * sigmap() - np.sqrt(0.1) * sigmam() #reservorio comprimido 
aest0 = qeye(2)
aest1 = projection(2,0,0)
aest2 = projection(2,1,1)
abest0 = bell_state(00)
abest1 = bell_state(10)
abest2 = pdrojection(4,1,1)
abest3 = projection(4,3,3) 
abest4 = projection(4,0,0)
times = np.linspace(int(0.0), int(10.0), int(60.0))
result1 = mesolve(H2, aest0, times)
result2 = mesolve(H2, aest1, times)
result3 = mesolve(H2, aest2, times)
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
