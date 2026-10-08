# Claim: "The nucleus's pull favours small patterns, the bending cost favours large ones, and the bottom rung is where they balance"
import sympy as sp
a, hb, m, kk, r = sp.symbols('a hbar m k r', positive=True)
psi = sp.exp(-r/a)/sp.sqrt(sp.pi*a**3)
T = sp.integrate(psi*(-hb**2/(2*m))*sp.diff(r**2*sp.diff(psi, r), r)/r**2*4*sp.pi*r**2, (r, 0, sp.oo))
V = sp.integrate(psi**2*(-kk/r)*4*sp.pi*r**2, (r, 0, sp.oo))
print("<T>(a) =", sp.simplify(T), " (grows as a shrinks)  <V>(a) =", sp.simplify(V), " (more negative as a shrinks)")
sol = sp.solve(sp.diff(T+V, a), a)
Emin = sp.simplify((T+V).subs(a, sol[0]))
print("minimum at a =", sol, " E_min =", Emin)
# numeric
from scipy import constants as c
import math
kv = c.e**2/(4*math.pi*c.epsilon_0)
a_num = c.hbar**2/(c.m_e*kv); E_num = -c.m_e*kv**2/(2*c.hbar**2)/c.e
print(f"a = {a_num:.4e} m (Bohr radius {c.physical_constants['Bohr radius'][0]:.4e}); E = {E_num:.3f} eV")
ok = sp.simplify(sol[0] - hb**2/(m*kk)) == 0 and abs(E_num + 13.6) < 0.01
print("PASS" if ok else "FAIL")
