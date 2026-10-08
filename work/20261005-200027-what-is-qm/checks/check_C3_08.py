# Claims: "an electron on a higher rung drops down sooner or later, giving off light";
# "from the bottom of the ladder there is nowhere lower to go"; "ladders of allowed energies for anything
# trapped"; "no two electrons can be in exactly the same state"; Check yourself: three rungs -> at most 3 lines
import sympy as sp, numpy as np
from itertools import combinations
from scipy.optimize import brentq
from scipy.constants import hbar, e, epsilon_0, c, physical_constants as pc
x = sp.symbols('x', positive=True)
R10 = 2*sp.exp(-x); R21 = x*sp.exp(-x/2)/(2*sp.sqrt(6))
zme = sp.integrate(R10*R21*x**3,(x,0,sp.oo))/sp.sqrt(3)
a0 = pc['Bohr radius'][0]; Ry = pc['Rydberg constant times hc in eV'][0]; w = 0.75*Ry*e/hbar
A = w**3*e**2*(float(zme)*a0)**2/(3*np.pi*epsilon_0*hbar*c**3)
print(f"A(2p->1s) = {A:.3e} /s (lifetime {1e9/A:.2f} ns); 2s decays by two photons (8.23 /s, literature)")
ok_low = all(-1/1 < -1/n**2 for n in range(2,1000)); print("n=1 is the lowest level:", ok_low)
pairs = list(combinations([1,2,3],2)); E = {n:-13.6/n**2 for n in (1,2,3)}
gaps = sorted(E[j]-E[i] for i,j in pairs); print("3 rungs ->", len(pairs), "distinct gaps:", np.round(gaps,3))
x1,x2 = sp.symbols('x1 x2'); f = sp.Function('f'); print("antisym f(x1)f(x2):", sp.simplify(f(x1)*f(x2)-f(x2)*f(x1)))
V0 = 50.0
def ev(E): kk,q = np.sqrt(E),np.sqrt(V0-E); return kk*np.sin(kk)-q*np.cos(kk)
def od(E): kk,q = np.sqrt(E),np.sqrt(V0-E); return kk*np.cos(kk)+q*np.sin(kk)
Es = np.linspace(1e-6,V0-1e-6,200001); roots = []
for g in (ev,od):
    v = g(Es); idx = np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0]
    roots += [brentq(g,Es[i],Es[i+1]) for i in idx if abs(v[i]) < 50]
print("finite well bound energies (discrete):", np.round(sorted(roots),3))
ok = A > 1e6 and ok_low and len(pairs)==3 and len(set(np.round(gaps,6)))==3 and 1 <= len(roots) < 20
print("PASS" if ok else "FAIL")
