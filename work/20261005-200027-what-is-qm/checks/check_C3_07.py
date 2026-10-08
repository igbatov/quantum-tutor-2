# Claims: "squeezed into less space wiggles more sharply ... more energy of motion";
# "The bottom rung is the best balance between pull and wiggle"; "lowest state the cloud is a round,
# fuzzy ball and nothing orbits"; "measure the electron's speed ... usually get more than a thousand km/s"
import sympy as sp, numpy as np
from scipy.constants import hbar, m_e, m_p, e, epsilon_0, c, physical_constants as pc
from scipy.integrate import quad
r,b,hb,m,k = sp.symbols('r b hbar m k', positive=True); th,ph = sp.symbols('theta phi', real=True)
psi = sp.exp(-r/b)/sp.sqrt(sp.pi*b**3)
T = sp.simplify(sp.integrate(4*sp.pi*r**2*psi*(-hb**2/(2*m))*sp.diff(r**2*sp.diff(psi,r),r)/r**2,(r,0,sp.oo)))
V = sp.simplify(sp.integrate(4*sp.pi*r**2*psi**2*(-k/r),(r,0,sp.oo)))
bmin = sp.solve(sp.diff(T+V,b),b)[0]; Emin = (T+V).subs(b,bmin)
kv = e**2/(4*np.pi*epsilon_0)
En = float(Emin.subs({hb:hbar,m:m_e,k:kv}))/e; bn = float(bmin.subs({hb:hbar,m:m_e,k:kv}))
print("<T> =",T,"(grows as b shrinks); <V> =",V,f"; best b = {bn/pc['Bohr radius'][0]:.4f} a0, E = {En:.3f} eV")
ok_bal = sp.diff(T,b).is_negative and abs(En+13.606) < 0.01
ok_round = not (psi.has(th) or psi.has(ph)); jcur = sp.im(sp.conjugate(psi)*sp.diff(psi,r))
print("no angle dependence:", ok_round, "; probability current:", jcur, "; L = 0 for 1s")
# momentum distribution of 1s (reduced mass): P(x) = 32/pi x^2/(1+x^2)^4, x = p/p0, p0 = hbar/a_mu
a_mu = pc['Bohr radius'][0]*(1+m_e/m_p); v0 = hbar/(m_e*a_mu)
P = lambda x: 32/np.pi*x**2/(1+x**2)**4
print(f"norm = {quad(P,0,np.inf)[0]:.8f}; v0 = {v0:.4e} m/s")
frac = quad(P, 1e6/v0, np.inf)[0]
print(f"P(speed > 1000 km/s) = {frac:.4f}")
for vv in [5e5, 1e6, 2e6]: print(f"  P(v > {vv/1e3:.0f} km/s) = {quad(P, vv/v0, np.inf)[0]:.3f}")
ok_speed = frac > 0.5
print("'usually more than a thousand km/s' (majority of measurements):", ok_speed, f"({100*frac:.1f}%)")
print("PASS" if ok_bal and ok_round and sp.simplify(jcur)==0 and ok_speed else "FAIL")
