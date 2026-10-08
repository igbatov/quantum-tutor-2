# Claim: "close in, that cost grows faster than the pull. Their balance sets the size ...
#         roughly a ten-billionth of a metre across"
# Heuristic energy E(r) = hbar^2/(2 m r^2) - k e^2/r ; minimize.
import sympy as sp
from scipy import constants as C
r, hb, m, k, e = sp.symbols('r hbar m k e', positive=True)
E = hb**2/(2*m*r**2) - k*e**2/r
rmin = sp.solve(sp.diff(E, r), r)[0]
Emin = sp.simplify(E.subs(r, rmin))
print("r_min =", rmin, "  E_min =", Emin)
# ratio cost/pull as r->0 diverges
ratio = sp.limit((hb**2/(2*m*r**2))/(k*e**2/r), r, 0)
print("cost/pull as r->0:", ratio)
vals = {hb: C.hbar, m: C.m_e, k: 1/(4*sp.pi.evalf()*C.epsilon_0), e: C.e}
rnum = float(rmin.subs(vals)); Enum = float(Emin.subs(vals))/C.e
print(f"r_min = {rnum:.3e} m (Bohr radius), diameter = {2*rnum:.3e} m; E_min = {Enum:.3f} eV")
ok = ratio == sp.oo and 0.3e-10 < 2*rnum < 3e-10
print("PASS" if ok else "FAIL")
