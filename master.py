from qutip import *
from matplotlib.pyplot import *
import numpy as np
H = np.sqrt(1.1) * sigmap() - np.sqrt(0.1) * sigmam()
psi0 = projection(2,0,1)
times = np.linspace(int(0.0), int(10.0), int(200.0))
result = mesolve(H, psi0, times, [], [])
#figure()
#plot(times, result.expect[0])
#plot(times, result.expect[1])
#xlabel('Tiempo')
#ylabel('Valores de Expectacion')
#legend(('numero de fotones en cavidad', 'probabilidad de excitacion atomica'))
#show()
