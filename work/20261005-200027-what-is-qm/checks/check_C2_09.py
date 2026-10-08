# Claims: "only certain patterns are steady, keeping their shape with one definite energy";
# "An electron on a higher rung soon drops anyway, by giving off light";
# "from the bottom rung there is nowhere lower to go"
import sympy as sp, numpy as np
from scipy.constants import hbar, e, epsilon_0, c, physical_constants as pc
r, a0, t, E, hb = sp.symbols('r a0 t E hbar', positive=True)
psi = sp.exp(-r/a0); Psi = psi*sp.exp(-sp.I*E*t/hb)
ok_stat = not sp.simplify(Psi*sp.conjugate(Psi)).has(t)
# a superposition of two energies is NOT steady
E1,E2 = sp.symbols('E1 E2', positive=True); f1,f2 = sp.symbols('f1 f2', positive=True)
S = f1*sp.exp(-sp.I*E1*t/hb)+f2*sp.exp(-sp.I*E2*t/hb)
ok_sup = sp.simplify(sp.expand(S*sp.conjugate(S))).has(t)
print("eigenstate density steady:", ok_stat, "; two-energy mix changes in time:", ok_sup)
# 2p -> 1s spontaneous emission rate: A = omega^3 e^2 |<1s|z|2p0>|^2 / (3 pi eps0 hbar c^3)
x = sp.symbols('x', positive=True)
R10 = 2*sp.exp(-x); R21 = x*sp.exp(-x/2)/(2*sp.sqrt(6))
radial = sp.integrate(R10*R21*x**3,(x,0,sp.oo))          # in units of a0
zme = radial/sp.sqrt(3)                                      # angular factor for m=0
print("<1s|z|2p0>/a0 =", sp.nsimplify(zme), "=", float(zme))
a0v = pc['Bohr radius'][0]; Ry = pc['Rydberg constant times hc in eV'][0]
w = 0.75*Ry*e/hbar
A = w**3*e**2*(float(zme)*a0v)**2/(3*np.pi*epsilon_0*hbar*c**3)
print(f"A(2p->1s) = {A:.3e} /s, lifetime = {1/A*1e9:.2f} ns")
print("2s lifetime (two-photon, literature 8.229 /s): 0.122 s -- not computed here")
# hydrogenic levels -13.6/n^2: n=1 is the minimum
ok_low = all(-13.6/1 < -13.6/n**2 for n in range(2,100))
print("PASS" if ok_stat and ok_sup and 1/A < 1e-8 and ok_low else "FAIL")
