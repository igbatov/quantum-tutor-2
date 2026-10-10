# Claim: "a state of definite energy E carries a frequency E/h while nothing observable about it
# changes (its hand turns at fixed length)".
import sympy as sp
E, t, hbar = sp.symbols('E t hbar', positive=True); phi0 = sp.symbols('phi0')
psi = phi0*sp.exp(-sp.I*E*t/hbar)
ok = sp.simplify(sp.diff(sp.Abs(psi)**2, t)) == 0
h = 2*sp.pi*hbar
period = 2*sp.pi*hbar/E           # time for the hand to make one turn
ok &= sp.simplify(1/period - E/h) == 0
print('|psi|^2 time-independent:', ok, '| frequency =', sp.simplify(1/period), '= E/h')
print('PASS' if ok else 'FAIL')
