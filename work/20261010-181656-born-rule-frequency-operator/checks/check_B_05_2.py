# Claim: "amplitude of size sin(Omega t/2) for up and cos(Omega t/2) for down"; "points trace sin^2(Omega t/2)";
# "pulse's length, or how far it is tuned ... sets a share p anywhere between 0 and 1"
import sympy as sp, numpy as np
from scipy.linalg import expm
W,t=sp.symbols('Omega t',positive=True)
sx=sp.Matrix([[0,1],[1,0]])
U=sp.simplify((-sp.I*W*t/2*sx).exp())
psi=sp.simplify(U*sp.Matrix([1,0]))   # (down, up)
print("final state (down, up):",list(psi))
ok = sp.simplify(sp.Abs(psi[0])**2-sp.cos(W*t/2)**2)==0 or sp.simplify(sp.expand_complex(psi[0]*sp.conjugate(psi[0]))-sp.cos(W*t/2)**2)==0
ok2= sp.simplify(sp.expand_complex(psi[1]*sp.conjugate(psi[1]))-sp.sin(W*t/2)**2)==0
# detuning at fixed pi-pulse: range of p
Om=1.0;tp=np.pi/Om;ps=[]
for D in np.linspace(0,10,20001):
    H=0.5*np.array([[-D,Om],[Om,D]]); ps.append(abs((expm(-1j*H*tp)@[1,0])[1])**2)
print("detuning scan at fixed pi pulse: p from",min(ps),"to",max(ps))
ok3=min(ps)<1e-4 and max(ps)>1-1e-9
print("PASS" if (ok or ok2) and ok2 and ok3 else "FAIL")
