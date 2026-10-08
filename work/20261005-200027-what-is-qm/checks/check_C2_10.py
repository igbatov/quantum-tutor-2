# Claims: Check yourself "only three rungs ... how many different colors, at most" (intended answer 3);
# "no two electrons can be in exactly the same state"; "energy ladders for anything trapped"
import sympy as sp, numpy as np
from itertools import combinations
from scipy.optimize import brentq
pairs = list(combinations([1,2,3],2)); E = {n:-13.6/n**2 for n in [1,2,3]}
gaps = [E[j]-E[i] for i,j in pairs]
print("3 rungs ->", len(pairs), "gaps:", np.round(gaps,3), "eV; hydrogen wavelengths nm:",
      [round(1239.84/g,1) for g in gaps])
# Pauli: antisymmetric two-electron state with both in the same state vanishes
x1,x2 = sp.symbols('x1 x2'); f = sp.Function('f')
print("antisymmetrized f(x1)f(x2) =", sp.simplify(f(x1)*f(x2)-f(x2)*f(x1)))
# trapped particle: finite square well (depth V0, half-width a), units hbar=2m=1 -> discrete bound energies
V0, a = 50.0, 1.0
def even(E): k=np.sqrt(E); q=np.sqrt(V0-E); return k*np.sin(k*a)-q*np.cos(k*a)
def odd(E):  k=np.sqrt(E); q=np.sqrt(V0-E); return k*np.cos(k*a)+q*np.sin(k*a)
Es=np.linspace(1e-6,V0-1e-6,200001); roots=[]
for g in (even,odd):
    v=g(Es); idx=np.where(np.sign(v[:-1])!=np.sign(v[1:]))[0]
    roots+= [brentq(g,Es[i],Es[i+1]) for i in idx if abs(v[i])<50]
print("finite well bound energies (discrete):", np.round(sorted(roots),3))
print("PASS" if len(pairs)==3 and len(set(np.round(gaps,6)))==3 and 1<=len(roots)<20 else "FAIL")
