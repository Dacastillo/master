tic


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ATOM %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Sistema de tres niveles
v3 = [1 0 0]';
v2 = [0 1 0]';
v1 = [0 0 1]';

% Operadores sistema tres niveles
Natom = 3;
sigma12 = v1*v2'; sigma21 = sigma12';
sigma23 = v2*v3'; sigma32 = sigma23';
sigma33 = v3*v3'; sigma11 = v1*v1';
Iatom = eye(Natom);

% Hamiltoniano del sistma de tres niveles (Referencia energia E2 = 0) 
w23 = 2; w12 = 3;
Hatom = w23*sigma33-w12*sigma11;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%% CAVITY MODES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Numero de fotones (dos modos: a y b)
Na = 2;
Nb = 2;

% Frecuencia cavidades 
wa = 0.9*w12;
wb = 0.9*w23;

% Dimension espacio de Hilbert
dima = Na+1;
dimb = Nb+1;

% Operadores modos
Ia = eye(dima);
Ib = eye(dimb);

% operador de destruccion modo a
a = diag(sqrt(1:Na)',1);
b = diag(sqrt(1:Nb)',1);

Nmod_a = a'*a;
[Va,Da] = eig(Nmod_a);
n1_a = Va(:,Na);  % 1 foton

Nmod_b = b'*b;
[Vb,Db] = eig(Nmod_b);
n1_b = Vb(:,Nb);  % 1 foton

a = kron(a,Ib);
b = kron(Ia,b);

% Hamiltoniano cavidades
Nmod_a = a'*a; Nmod_b = b'*b;
Hcav = wa*Nmod_a + wb*Nmod_b;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%  HAMILTONIANO SISTEMA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Constantes de acoplamiento atomo-cavidad
ga = 0.1*wa;
gb = 0.1*wb;

% Hamiltoniano del sistemas atomo-cavidad
H0 = kron(Hatom,kron(Ia,Ib))+kron(Iatom,Hcav);
Hcoupling = ga*(kron(sigma12,a')+kron(sigma21,a))+gb*(kron(sigma23,b')+kron(sigma32,b));
Hsys = H0+Hcoupling;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%  ECUACION MAESTRA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

wmax = max(w23,w12);
wmin = min(w23,w12);


% Time vector
Nt = 1000;
tmin = 1e-2*1/wmax;
tmax = 1e+2*1/wmin;
dt = (tmax-tmin)/(Nt-1);
t = tmin:dt:tmax;

% Operador densidad estado inicial
rho_atom_0 = v2*v2';
rho_a_0 = n1_a*n1_a';
rho_b_0 = n1_b*n1_b';

% Estado inicial
rho_0 = kron(rho_atom_0,kron(rho_a_0,rho_b_0));
rho = rho_0;

% Perdidas atomicas
gamma12 = 0.01*ga;
gamma23 = 0.01*gb;

% Perdidas de las cavidades
eta_a = 2;
eta_b = eta_a;

% Perdidas de la cavidad
gamma_a = 0.01*4*ga^2/(eta_a*gamma12);
gamma_b = 0.01*4*gb^2/(eta_b*gamma23);

% Operadores en el espacio de Hilbert completo
a = kron(Iatom,a);
b = kron(Iatom,b);
sigma12 = kron(sigma12,kron(Ia,Ib));
sigma23 = kron(sigma23,kron(Ia,Ib));

% Observables
Tr_rho = zeros(size(t));
a_prom = zeros(size(t));

for j=1:Nt
    nk = 10;   % Iteraciones dentro del ciclo for para mejorar la precision numerica

    for k=1:nk
        
        % Perdidas de las cavidades
        La = gamma_a*(2*a*rho*a'-a'*a*rho-rho*(a')*a);
        Lb = gamma_b*(2*b*rho*b'-b'*b*rho-rho*(b')*b);
        
        % Perdidas atomicas
        L12 = gamma12*(2*sigma12*rho*(sigma12')-sigma12'*sigma12*rho-rho*(sigma12')*sigma12);
        L23 = gamma23*(2*sigma23*rho*(sigma23')-sigma23'*sigma23*rho-rho*(sigma23')*sigma23);
        
        % Evolucion del atomo libre
        L_atom = -1i*(Hsys*rho-rho*Hsys);
        
        L = L_atom + La + Lb + L12 + L23;
        rho_pred = rho + L*dt/nk;
        rho_m = 0.5*(rho+rho_pred);
        
        % Perdidas de las cavidades
        La = gamma_a*(2*a*rho_m*a'-a'*a*rho_m-rho_m*(a')*a);
        Lb = gamma_b*(2*b*rho_m*b'-b'*b*rho_m-rho_m*(b')*b);
        
        % Perdidas atomicas
        L12 = gamma12*(2*sigma12*rho_m*(sigma12')-sigma12'*sigma12*rho_m-rho_m*(sigma12')*sigma12);
        L23 = gamma23*(2*sigma23*rho_m*(sigma23')-sigma23'*sigma23*rho_m-rho_m*(sigma23')*sigma23);
        
        % Evolucion del atomo libre
        L_atom = -1i*(Hsys*rho_m-rho_m*Hsys);
        L = L_atom + La + Lb + L12 + L23;
        rho = rho + L*dt/nk;
        
    end
 
    % Traza operador densidad total
    %Tr_rho(j) = trace(rho);
    
    % Promedio operador a$
    a_prom(j) = trace((a')*a*rho);
    
    
end


figure(1)
box on
hold on
%plot(t,real(Tr_rho),'r--','Linewidth',1.5)
%plot(t,imag(Tr_rho),'b--','Linewidth',1.5)
plot(t,a_prom)
hold off
%xlabel('$\mbox{Time}$','Interpreter','LaTex','Fontsize', 21)
%ylabel('$\mbox{Tr}[\rho(t)]$','Interpreter','LaTex','Fontsize', 21)
%set(gca,'fontsize',21)
%legend({'$\mbox{real}$','$\mbox{imag}$'},'Interpreter','latex','Fontsize', 21,'Location','northeast')


toc