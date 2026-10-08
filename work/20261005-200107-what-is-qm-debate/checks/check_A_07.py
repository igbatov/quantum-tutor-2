# Claim: "squeezing the wave closer forces in shorter wavelengths, so more energy of motion, a cost that balances the nucleus's pull"
# Estimate: E(r) = hbar^2/(2 m r^2) - e^2/(4 pi eps0 r); minimum should give Bohr radius and -13.6 eV.
import sympy as sp
from scipy.constants import hbar, m_e, e, epsilon_0, physical_constants
r = sp.symbols('r', positive=True)
hb, m, q, eps = sp.symbols('hbar m e epsilon0', positive=True)
E = hb**2/(2*m*r**2) - q**2/(4*sp.pi*eps*r)
rmin = sp.solve(sp.diff(E, r), r)[0]
Emin = sp.simplify(E.subs(r, rmin))
vals = {hb: hbar, m: m_e, q: e, eps: epsilon_0}
r0 = float(rmin.subs(vals)); E0 = float(Emin.subs(vals))/e
a0 = physical_constants['Bohr radius'][0]
print("r_min =", rmin, "=", r0, "m; Bohr radius =", a0)
print("E_min =", Emin, "=", E0, "eV")
ok = abs(r0-a0)/a0 < 1e-6 and abs(E0 + 13.6057) < 0.01
print("PASS" if ok else "FAIL")
