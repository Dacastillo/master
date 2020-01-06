import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
eps= h5py.File('cav-eps-000000.00.h5','r')
deps=eps['eps']
dpwr0= h5py.File('cav-denergy-001200.00.h5','r')
ddpwr0=dpwr0['denergy']
dpwr1= h5py.File('cav-denergy-001300.00.h5','r')
ddpwr1=dpwr1['denergy']
dpwr2= h5py.File('cav-denergy-001400.00.h5','r')
ddpwr2=dpwr2['denergy']
efiex0= h5py.File('cav-ex-001200.00.h5','r')
defiex0=efiex0['ex']
efiex1= h5py.File('cav-ex-001300.00.h5','r')
defiex1=efiex1['ex']
efiex2= h5py.File('cav-ex-001400.00.h5','r')
defiex2=efiex2['ex']
hfiex0= h5py.File('cav-hx-001200.00.h5','r')
dhfiex0=hfiex0['hx']
hfiex1= h5py.File('cav-hx-001300.00.h5','r')
dhfiex1=hfiex1['hx']
hfiex2= h5py.File('cav-hx-001400.00.h5','r')
dhfiex2=hfiex2['hx']
efiey0= h5py.File('cav-ey-001200.00.h5','r')
defiey0=efiey0['ey']
efiey1= h5py.File('cav-ey-001300.00.h5','r')
defiey1=efiey1['ey']
efiey2= h5py.File('cav-ey-001400.00.h5','r')
defiey2=efiey2['ey']
hfiey0= h5py.File('cav-hy-001200.00.h5','r')
dhfiey0=hfiey0['hy']
hfiey1= h5py.File('cav-hy-001300.00.h5','r')
dhfiey1=hfiey1['hy']
hfiey2= h5py.File('cav-hy-001400.00.h5','r')
dhfiey2=hfiey2['hy']
efiez0= h5py.File('cav-ez-001200.00.h5','r')
defiez0=efiez0['ez']
efiez1= h5py.File('cav-ez-001300.00.h5','r')
defiez1=efiez1['ez']
efiez2= h5py.File('cav-ez-001400.00.h5','r')
defiez2=efiez2['ez']
hfiez0= h5py.File('cav-hz-001200.00.h5','r')
dhfiez0=hfiez0['hz']
hfiez1= h5py.File('cav-hz-001300.00.h5','r')
dhfiez1=hfiez1['hz']
hfiez2= h5py.File('cav-hz-001400.00.h5','r')
dhfiez2=hfiez2['hz']
a0=np.array(defiex0[0:195][0:85])*np.array(defiex0[0:195][0:85])+np.array(defiey0[0:195][0:85])*np.array(defiey0[0:195][0:85])+np.array(defiez0[0:195][0:85])*np.array(defiez0[0:195][0:85])
a1=np.array(defiex1[0:195][0:85])*np.array(defiex1[0:195][0:85])+np.array(defiey1[0:195][0:85])*np.array(defiey1[0:195][0:85])+np.array(defiez1[0:195][0:85])*np.array(defiez1[0:195][0:85])
a2=np.array(defiex2[0:195][0:85])*np.array(defiex2[0:195][0:85])+np.array(defiey2[0:195][0:85])*np.array(defiey2[0:195][0:85])+np.array(defiez2[0:195][0:85])*np.array(defiez2[0:195][0:85])
ep=deps[0:195][0:85]
i0= np.array(np.multiply(a0,np.multiply(a0,ep)))
i1= np.array(np.multiply(a1,np.multiply(a1,ep)))
i2= np.array(np.multiply(a2,np.multiply(a2,ep)))
q0= a0*a0
q1= a1*a1
q2= a2*a2
V0=0
V1=1
V2=2
A0=0
A1=0
A2=0
B0=0
B1=0
B2=0
Neff0=0
Neff1=0
Neff2=0
for j in range (0,85):
    for k in range (0,85):
        V0=V0+(i0[j][k]/i0.max())/(195*85) 
        V1=V1+(i1[j][k]/i0.max())/(195*85) 
        V2=V2+(i2[j][k]/i0.max())/(195*85) 
        A0=A0+i0[j][k]/(195*85)
        A1=A1+i1[j][k]/(195*85)
        A2=A2+i2[j][k]/(195*85)
        B0=B0+q0[j][k]/(195*85)
        B1=B1+q1[j][k]/(195*85)
        B2=B2+q2[j][k]/(195*85)
Neff0=A0/B0
Neff1=A1/B1
Neff2=A2/B2
Veff0=V0/1
Veff1=V1/1
Veff2=V2/1
print(Veff0,Veff1,Veff2)
print(Neff0,Neff1,Neff2)
