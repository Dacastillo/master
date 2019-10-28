import matplotlib.pyplot as plt
from qutip import *
from pylab import *
from numpy import *
from scipy import *
from math import exp
Nmax_osc = 15 #Número máximo de osciladores
wm = 1.0
wc = 100*wm
wa = 110*wm
k = 0.3 #cavity-oscillator coupling
g = 0.5 #cavity-atom J coupling
nth = 0.5
tin = 0
tfin = 0.6
nt1 = 30
nt2 = 50
dt = 7*tfin
print(Nmax_osc, wm, wc, wa, k, g, nth, tin, tfin, nt1, nt2, dt)
tlist1 = linspace(tin,tfin,nt1)
tlist2 = linspace(tin,dt,nt2)
d = basis(2,1)
u = basis(2,0)
rho0_osc = thermal_dm(Nmax_osc + 1, nth)
rho0_cav = thermal_dm(Nmax_osc + 1, nth)
rho_ini = rho0_cav
a1 = tensor(qeye(2), destroy(Nmax_osc + 1), qeye(Nmax_osc + 1)) #phonon operator
a2 = tensor(destroy(Nmax_osc + 1), qeye(Nmax_osc + 1))
c1 = tensor(qeye(2), qeye(Nmax_osc + 1), destroy(Nmax_osc + 1)) #cavity operator
c2 = tensor(qeye(Nmax_osc + 1), destroy(Nmax_osc + 1))
b = destroy(Nmax_osc + 1) #lasing mode
sz = tensor(sigmaz(), qeye(Nmax_osc + 1), qeye(Nmax_osc + 1))
sm = tensor(sigmam(), qeye(Nmax_osc + 1), qeye(Nmax_osc + 1))
sp = tensor(sigmap(), qeye(Nmax_osc + 1), qeye(Nmax_osc + 1))
n_m1 = (a1.dag())*a1
n_cav1 = (c1.dag())*c1
x1 = (a1.dag())+a1
n_m2 = (a2.dag())*a2
n_cav2 = (c2.dag())*c2
x2 = (a2.dag())+a2
H1 = wa*sz*0.5 + n_m1 + wc*n_cav1 - k*n_cav1*x1 + g*(sp*c1+sm*c1.dag())
H2 = n_m2 + wc*n_cav2 - k*n_cav2*x2
H_rel = (b.dag())*b #- (b.dag())*b
nm = nth
gammas = 10**(-3)*0 #a few miliseconds
gammaphi = 10**(-2)*0
gamma_m = 0.002  #mechanics losses
gamma_c = 0.02 #cavity losses
c_ops1 = []
c_ops2 = []
c_relax = []
gamma1 = 0
# Mechanical damping rate
c_ops1.append( sqrt( gamma_m*(1+nm) ) * a1 + sqrt( gamma_c*(1+nm) ) * c1)
c_ops1.append( sqrt( gamma_m* nm) * a1.dag() + sqrt( gamma_c*nm ) * c1 )
# Mechanical & cavity damping rate
c_ops2.append( sqrt( gamma_m*(1+nm) ) * a2 + sqrt( gamma_c*(1+nm) ) * c2)
#c_ops2.append( sqrt( gamma_c*(1+nm) ) * c2)
c_ops2.append( sqrt( gamma_m* nm) * a2.dag() + sqrt( gamma_c*nm ) * c2.dag())
#c_ops2.append( sqrt( gamma_c*nm ) * c2.dag())
#damping during relaxation time
c_relax.append( sqrt( gamma_c*(1+nm) ) * b)
c_relax.append( sqrt( gamma_c * nm ) * b.dag() )
rate=1/dt
Nit=20
n_cav1 =[]
n_osc1 =[]
n_cav2 =[]
n_osc2 =[]
g2_cav =[]
g2_osc=[]
vector_x = []
dx_cav1= []
dx_cav2= []
dx_osc1= []
dx_osc2= []
dp_cav1= []
dp_cav2= []
dp_osc1= []
dp_osc2= []
nom0=expect( b.dag()*b.dag()* b*b , rho_ini)
den0=expect( b.dag() * b, rho_ini)
g2_cav.append(nom0/(den0**2))
g2_osc.append(nom0/(den0**2))
n_cav1.append(den0)
n_osc1.append(den0)
n_cav2.append(den0)
n_osc2.append(den0)
dx_cav1.append(variance((b + b.dag())*0.5, rho0_cav))
dx_cav2.append(variance((b + b.dag())*0.5, rho0_cav))
dx_osc1.append(variance((b + b.dag())*0.5, rho0_osc))
dx_osc2.append(variance((b + b.dag())*0.5, rho0_osc))
dp_cav1.append(variance((b.dag() - b)*1j*0.5, rho0_cav))
dp_cav2.append(variance((b.dag() - b)*1j*0.5, rho0_cav))
dp_osc1.append(variance((b.dag() - b)*1j*0.5, rho0_osc))
dp_osc2.append(variance((b.dag() - b)*1j*0.5, rho0_osc))
vector_x.append(0)
rho_cav1 = rho0_cav
#Preselection
psi0_atom_aux = (u).unit()
rho0_atom = psi0_atom_aux * psi0_atom_aux.dag()
rho0 = tensor(rho0_atom, rho0_osc, rho0_cav)
#Postselection
phi1 = 0
theta1 = pi
Psi_qubit1 = (cos(theta1*0.5)*u + sin(theta1*0.5)*d).unit()
Ket_Psipost1 = tensor(Psi_qubit1, qeye(Nmax_osc +1), qeye(Nmax_osc +1))
Bra_Psipost1 = Ket_Psipost1.dag()
projector = Ket_Psipost1*Bra_Psipost1

for t in arange(1, Nit): 
          
        #Evolution with full interaction and only oscillator's decoherence 
        evol_inter= mesolve(H1, rho0, tlist1, c_ops1, []) #
        
#        rho_ss = steadystate(H1, c_ops1) 
        
        rho_tot = (evol_inter.states[len(tlist1)-1]).unit() #t = pi (losses)
        #rho_osc_qub = rho_ss
        
        # Postselecting
        rho_post = (Bra_Psipost1*rho_tot*Ket_Psipost1).unit()
        
        # partial trace on spin
        #rho_post = (ptrace(rho_tot,[1,2])).unit()
        
        # partial trace for cavity and oscillator
#        rho_osc1 = (ptrace(rho_post,[0])).unit()
#        rho_cav1 = (ptrace(rho_post,[1])).unit()
        
#        n_cav1.append(expect( b.dag() * b , rho_cav1))
#        n_osc1.append(expect( b.dag() * b , rho_osc1))
        
#        dx_cav1.append(variance((b + b.dag())*0.5, rho_cav1))
#        dp_cav1.append(variance(1j*(b.dag()-b)*0.5, rho_cav1))
#        dx_osc1.append(variance((b + b.dag())*0.5, rho_osc1))
#        dp_osc1.append(variance(1j*(b.dag()-b)*0.5, rho_osc1))
        
        rho_t = rho_post
        
        #Evolution with both decoherences 
        evol_exch = mesolve(H2, rho_t, tlist2, c_ops2, [])
        
        rho_aux = (evol_exch.states[len(tlist2)-1]).unit()
        
        rho_osc2 = (ptrace(rho_aux,[0])).unit()
        rho_cav2 = (ptrace(rho_aux,[1])).unit()
        
        rho0 = tensor(rho0_atom, rho_aux)
                
#        n_cav2.append(expect( b.dag() * b , rho_cav2))
#        n_osc2.append(expect( b.dag() * b , rho_osc2))
        
#        nom_cav=expect( b.dag()*b.dag()* b*b , rho_cav2)
#        den_cav=expect( b.dag() * b , rho_cav2)
#        nom_osc=expect( b.dag()*b.dag()* b*b , rho_osc2)
#        den_osc=expect( b.dag() * b , rho_osc2)
        
#        g2_cav.append(nom_cav/(den_cav**2))
#        g2_osc.append(nom_osc/(den_osc**2))
        
#        dx_cav2.append(variance((b + b.dag())*0.5, rho_cav2))
#        dp_cav2.append(variance(1j*(b.dag()-b)*0.5, rho_cav2))
#        dx_osc2.append(variance((b + b.dag())*0.5, rho_osc2))
#        dp_osc2.append(variance(1j*(b.dag()-b)*0.5, rho_osc2))

#        vector_x.append(t*dt)       
        #theta1 = theta1+pi*0.5

#print('rate/loss', rate/gammam) #should be very large  


#rc('text', usetex=False)
##print(' phonon - red  & photon -blue')
#fig, axes = plt.subplots(1, 1, figsize=(7,5))

#xlabel(r'$time$ [arb. units]')
#ylabel('$<n_c>, <n_m>$')

#plot(vector_x,n_osc2,'r') #oscillator
#plot(vector_x,n_cav2,'b') #cavity
#savefig("fig_aver.pdf", bbox_inches='tight')
#show()

#print(' phonon - red  & photon -blue')
#fig, axes = plt.subplots(1, 1, figsize=(7,5))
#g2_teor =[]
#line = []

#for t in arange(0, Nit): 
#    line.append(1)
    
#xlabel(r'$time$ [arb. units]')
#ylabel('$g^{(2)}(0)$')
#plot(vector_x,g2_teor,'r-.')
#plot(vector_x,real(g2_osc),'r')
#plot(vector_x,real(g2_cav),'b')
#plot(vector_x,line,'k--')
#savefig("fig_g2.pdf", bbox_inches='tight')
#show()


#print(' phonon - red & photon - blue: dx -- & dp **')

#fig, axes = plt.subplots(1, 1, figsize=(7,5))
#axes = plt.axes(xlim=(0, (Nit*dt)), ylim=(0, 3))

#H_insert = []
#line =[]

#dx=dx_osc2
#dp=dp_osc2

#for t in arange(0, Nit): 
#    H_insert.append(sqrt(dx[t]*dp[t]))
#    line.append(0.25)

#xlabel(r'$time$ [arb. units]')
#ylabel('$<\Delta x^2>$, $<\Delta p^2>$')

#plot(vector_x,dx_cav2,'b--')
#plot(vector_x,dx_osc2,'r--')

#plot(vector_x,dp_cav2,'b*')
#plot(vector_x,dp_osc2,'r*')

#plot(vector_x,line,'k--')

#savefig("fig_fluct.pdf", bbox_inches='tight')


b = destroy(Nmax_osc+1)
pdistr=[]
vector_n=[]

nav_osc = abs(expect( b.dag() * b , rho_osc2))
n0 = den0

#for n in arange(0, Nmax_osc+1):
#    pdistr.append(exp(-nav_osc)*nav_osc**n/misc.factorial(n))
#    vector_n.append(n)


#plot_fock_distribution(rho_osc2)
#plot(vector_n,pdistr,'r') 

#savefig("fig_Pdistr_osc.pdf", bbox_inches='tight')

#b = destroy(Nmax_osc+1)
#pdistr=[]
#vector_n=[]

#nav_cav = abs(expect( b.dag() * b , rho_cav2))
#n0 = den0

#for n in arange(0, Nmax_osc+1):
#    pdistr.append(exp(-nav_cav)*nav_cav**n/misc.factorial(n))
#    vector_n.append(n)

#plot_fock_distribution(rho_cav2)
#plot(vector_n,pdistr,'r') 

#savefig("fig_Pdistr_cav.pdf", bbox_inches='tight')

#plot_wigner_fock_distribution(rho_osc2)
#savefig("fig_wigner_osc.pdf", bbox_inches='tight')

#plot_wigner_fock_distribution(rho_cav2)
#savefig("fig_wigner_cav.pdf", bbox_inches='tight')
