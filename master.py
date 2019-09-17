from qutip import *
from matplotlib.pyplot import *
import numpy as np
H0 = sigmap() #reservorio vacio
H1 = np.sqrt(1.1) * sigmap() #reservorio termal
H2 = np.sqrt(1.1) * sigmap() - np.sqrt(0.1) * sigmam() #reservorio comprimido 
H0A = tensor([sigmap(),qeye(2)])
H0B = tensor([qeye(2),sigmap()])
H1A = np.sqrt(1.1) * tensor([sigmap(),qeye(2)]) 
H1B = np.sqrt(1.1) * tensor([qeye(2),sigmap()])
H2A = np.sqrt(1.1) * tensor([sigmap(),qeye(2)]) - np.sqrt(0.1) * tensor([sigmam(),qeye(2)])
H2B = np.sqrt(1.1) * tensor([qeye(2),sigmap()]) - np.sqrt(0.1) * tensor([qeye(2),sigmam()])
H0AB = H0A+H0B
H1AB = H1A+H1B
H2AB = H2A+H2B
aest0  = qeye(2)
aest1 = projection(2,0,0)
aest2 = projection(2,1,1)
abest0 = bell_state()
abest1 = bell_state()
abest2 = projection(4,1,1)
abest3 = projection(4,3,3) 
abest4 = projection(4,0,0)
times = np.linspace(int(0.0), int(10.0), int(200.0))
result1 = mesolve(H2, aest0, times)
result2 = mesolve(H2, aest1, times)
result3 = mesolve(H2, aest2, times)
result4 = mesolve(H2AB, abest2, times)
fin1 = result1.states[10]
fin2 = result1.states[20]
fin3 = result1.states[30]
fin4 = result2.states[10]
fin5 = result2.states[20]
fin6 = result2.states[30]
fin7 = result3.states[10]
fin8 = result3.states[20]
fin9 = result3.states[30]
finA = result4.states[50]
test0 = float( finA.eigenenergies()[3] )
#log0 = np.log2(-5.365778)
print( test0 )
print(abest0)
print(abest1)
#figure()
#plot(times, result.expect[0])
#plot(times, result.expect[1])
#xlabel('Tiempo')
#ylabel('Valores de Expectacion')
#legend(('numero de fotones en cavidad', 'probabilidad de excitacion atomica'))
#show()
