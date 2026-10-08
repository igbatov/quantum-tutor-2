# Claims: "a wave squeezed into less space wiggles more sharply ... more energy of motion";
# "The bottom rung is the best balance of the two"; "lowest state the cloud is a round ball";
# "nothing goes around"; "measure its speed and you'd find it moving fast";
# "size of that number, squared, gives the chance"
import sympy as sp, numpy as np
from scipy.constants import hbar, m_e, e, epsilon_0, c, physical_constants as pc
from scipy.integrate import quad
r, b, hb, m, k = sp.symbols('r b hbar m k', positive=True)
th, ph = sp.symbols('theta phi', real=True)
# exact variational family psi_b = exp(-r/b)/sqrt(pi b^3)
psi = sp.exp(-r/b)/sp.sqrt(sp.pi*b**3)
norm = sp.integrate(4*sp.pi*r**2*psi**2,(r,0,sp.oo))
T = sp.simplify(sp.integrate(4*sp.pi*r**2*psi*(-hb**2/(2*m))*sp.diff(r**2*sp.diff(psi,r),r)/r**2,(r,0,sp.oo)))
V = sp.simplify(sp.integrate(4*sp.pi*r**2*psi**2*(-k/r),(r,0,sp.oo)))
print("norm =", sp.simplify(norm), "; <T> =", T, "; <V> =", V)
bmin = sp.solve(sp.diff(T+V,b), b)[0]; Emin = sp.simplify((T+V).subs(b,bmin))
kv = e**2/(4*np.pi*epsilon_0)
bn = float(bmin.subs({hb:hbar,m:m_e,k:kv})); En = float(Emin.subs({hb:hbar,m:m_e,k:kv}))/e
print(f"best b = {bn:.4e} m (a0 = {pc['Bohr radius'][0]:.4e}); E = {En:.3f} eV")
ok_bal = sp.simplify(T - hb**2/(2*m*b**2))==0 and abs(bn/pc['Bohr radius'][0]-1)<1e-3 and abs(En+13.606)<0.01
# round: no angle dependence; current j = (hbar/m) Im(psi* grad psi) = 0 for real psi
ok_round = not (psi.has(th) or psi.has(ph)); j = sp.im(sp.conjugate(psi)*sp.diff(psi,r))
print("round ball:", ok_round, "; radial/angular probability current:", sp.simplify(j))
# momentum distribution of 1s: P(p) = (32/pi) p0^5 p^2/(p^2+p0^2)^4
P = lambda x: 32/np.pi*x**2/(1+x**2)**4   # x = p/p0, p0 = hbar/a0 ; v0 = alpha c
print("momentum norm =", round(quad(P,0,np.inf)[0],8))
cdf = lambda X: quad(P,0,X)[0]
from scipy.optimize import brentq
med = brentq(lambda X: cdf(X)-0.5, 0.01, 10); v0 = hbar/(m_e*pc['Bohr radius'][0])
print(f"rms speed = {v0:.3e} m/s; median speed = {med*v0:.3e} m/s")
for vv in [1e5, 1e4]:
    print(f"P(speed < {vv:.0e} m/s) = {cdf(vv/v0):.2e}")
ok_fast = med*v0 > 1e6 and cdf(1e5/v0) < 1e-3
print("PASS" if ok_bal and ok_round and sp.simplify(j)==0 and ok_fast and sp.simplify(norm-1)==0 else "FAIL")
