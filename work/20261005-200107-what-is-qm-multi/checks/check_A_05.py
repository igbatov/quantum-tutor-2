# Claim: lowest state "about a tenth of a nanometer (a ten-millionth of a millimeter) across"
# and "Squeezing a wave costs energy ... best balance": minimize E(r)=hbar^2/(2 m r^2) - k e^2/r
import sympy as sp
from scipy.constants import physical_constants as pc, hbar, m_e, e, epsilon_0, pi
r = sp.symbols('r', positive=True)
hb, m, k, q = sp.symbols('hbar m k q', positive=True)
E = hb**2/(2*m*r**2) - k*q**2/r
rmin = sp.solve(sp.diff(E, r), r)[0]
Emin = sp.simplify(E.subs(r, rmin))
print("r_min =", rmin, " E_min =", Emin)
subs = {hb:hbar, m:m_e, k:1/(4*pi*epsilon_0), q:e}
rv = float(rmin.subs(subs)); Ev = float(Emin.subs(subs))/e
a0 = pc['Bohr radius'][0]
print(f"r_min = {rv:.4e} m (a0 = {a0:.4e}); E_min = {Ev:.3f} eV")
diam = 2*a0
print(f"diameter ~ 2 a0 = {diam*1e9:.3f} nm; ten-millionth of mm = {1e-3/1e7:.1e} m")
ok = abs(rv-a0)/a0 < 1e-6 and abs(Ev+13.6) < 0.1 and 0.05e-9 < diam < 0.2e-9 and abs(1e-10 - 0.1e-9) < 1e-20
print("PASS" if ok else "FAIL")
