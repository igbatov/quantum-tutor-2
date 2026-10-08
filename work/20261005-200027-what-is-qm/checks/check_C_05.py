# Claims: "The bottom rung is the best balance" (squeezing raises kinetic energy, lowers potential);
# "in hydrogen's lowest state the cloud is a round ball"; "measure its speed ... moving fast";
# "size of that number, squared, gives the chance" (normalization); steady patterns "keeping their shape"
import sympy as sp
import numpy as np
from scipy.constants import hbar, m_e, e, epsilon_0, physical_constants as pc, c
a = sp.symbols('a', positive=True)
hb, m, k = sp.symbols('hbar m k', positive=True)
E = hb**2/(2*m*a**2) - k/a          # uncertainty-style estimate
amin = sp.solve(sp.diff(E,a), a)[0]
Emin = sp.simplify(E.subs(a, amin))
kval = e**2/(4*np.pi*epsilon_0)
amin_n = float(amin.subs({hb:hbar,m:m_e,k:kval})); Emin_n = float(Emin.subs({hb:hbar,m:m_e,k:kval}))/e
print("a_min =", amin, "=", amin_n, "m; Bohr radius", pc['Bohr radius'][0])
print("E_min =", Emin, "=", Emin_n, "eV")
ok1 = abs(amin_n/pc['Bohr radius'][0]-1)<1e-6 and abs(Emin_n+13.6057)<0.001
# exact ground state: psi = exp(-r/a0)/sqrt(pi a0^3), spherically symmetric, normalized
r, a0, th, ph, t, En = sp.symbols('r a0 theta phi t E', positive=True)
psi = sp.exp(-r/a0)/sp.sqrt(sp.pi*a0**3)
norm = sp.integrate(psi**2*r**2*sp.sin(th), (r,0,sp.oo),(th,0,sp.pi),(ph,0,2*sp.pi))
print("normalization =", sp.simplify(norm), "; psi depends on theta/phi:", psi.has(th) or psi.has(ph))
# <p^2> = hbar^2/a0^2 -> rms speed
lap = sp.diff(r**2*sp.diff(psi,r),r)/r**2
p2 = sp.simplify(sp.integrate(psi*(-lap)*4*sp.pi*r**2,(r,0,sp.oo)))  # in units hbar^2
print("<p^2>/hbar^2 =", p2)
v = hbar/(pc['Bohr radius'][0]*m_e)
print(f"rms speed = {v:.3e} m/s = {v/c:.4f} c (alpha = {pc['fine-structure constant'][0]:.4f})")
# stationary state: |psi e^{-iEt/hbar}|^2 independent of t
Psi = psi*sp.exp(-sp.I*En*t/hb)
dens = sp.simplify(Psi*sp.conjugate(Psi))
ok4 = not dens.has(t)
print("|Psi|^2 time-independent:", ok4)
ok = ok1 and sp.simplify(norm-1)==0 and not(psi.has(th) or psi.has(ph)) and sp.simplify(p2-1/a0**2)==0 and v>1e6 and ok4
print("PASS" if ok else "FAIL")
