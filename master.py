from qutip import *
from matplotlib.pyplot import *
import numpy as np
H = 2 * np.pi * 0.1 * sigmax()
psi0 = tensor(fock(2,0), fock(10,5))
a = tensor(qeye(2),destroy(10))
sm = tensor(destroy(2),qeye(10))
H = 2 * np.pi * a.dag()* a + 2 * np.pi *sm.dag() * sm  + 2 * np.pi * 0.25 * (sm * a.dag() + sm.dag()*a)
times = np.linspace(int(0.0), int(10.0), int(200.0))
result = mesolve(H, psi0, times, [np.sqrt(0.1) * a], [a.dag()*a, sm.dag()*sm])
figure()
plot(times, result.expect[0])
plot(times, result.expect[1])
xlabel('Tiempo')
ylabel('Valores de Expectacion')
legend(('numero de fotones en cavidad', 'probabilidad de excitacion atomica'))
show()
