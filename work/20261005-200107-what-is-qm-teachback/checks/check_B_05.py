# Claim: "There is a lowest pattern, the best compromise between staying near the nucleus ... and not being squeezed"
# Check: variational energy E(a) for 1s-type trial exp(-r/a) has a minimum at a = a0 with E = -13.6 eV.
import sympy as sp
from scipy.constants import physical_constants, hbar, m_e, e, epsilon_0, pi
a, r = sp.symbols('a r', positive=True)
hb, me, k = sp.symbols('hbar m_e k', positive=True)
psi = sp.exp(-r/a)
norm = sp.integrate(psi**2*4*sp.pi*r**2, (r, 0, sp.oo))
# kinetic <-hbar^2/2m lap>, = hbar^2/(2m) int |psi'|^2 dV
T = hb**2/(2*me)*sp.integrate(sp.diff(psi, r)**2*4*sp.pi*r**2, (r, 0, sp.oo))/norm
V = -k*sp.integrate(psi**2/r*4*sp.pi*r**2, (r, 0, sp.oo))/norm
Ea = sp.simplify(T + V)
amin = sp.solve(sp.diff(Ea, a), a)[0]
Emin = sp.simplify(Ea.subs(a, amin))
print("E(a) =", Ea, " a_min =", amin, " E_min =", Emin)
vals = {hb: hbar, me: m_e, k: e**2/(4*pi*epsilon_0)}
a_num = float(amin.subs(vals)); E_num = float(Emin.subs(vals))/e
print(f"a_min = {a_num:.4e} m (a0 = {physical_constants['Bohr radius'][0]:.4e}), E_min = {E_num:.3f} eV")
# kinetic rises as a shrinks, potential falls: genuine compromise
ok = abs(a_num/physical_constants['Bohr radius'][0]-1) < 1e-3 and abs(E_num+13.6) < 0.05
ok &= sp.limit(Ea, a, 0) == sp.oo
print("PASS" if ok else "FAIL")
