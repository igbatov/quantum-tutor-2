# Claim: "its energy is set by its shape alone" (wave can't be made louder; normalized to one electron)
# Energy <H>/<psi|psi> is invariant under psi -> c*psi; for 1D hydrogen-like radial test: use 1s.
import sympy as sp
r, a, c = sp.symbols('r a c', positive=True)
hb, m, k, e = sp.symbols('hbar m k e', positive=True)
psi = c*sp.exp(-r/a)
lap = sp.diff(r**2*sp.diff(psi, r), r)/r**2
Hpsi = -hb**2/(2*m)*lap - k*e**2/r*psi
num = sp.integrate(psi*Hpsi*4*sp.pi*r**2, (r, 0, sp.oo))
den = sp.integrate(psi**2*4*sp.pi*r**2, (r, 0, sp.oo))
Eexp = sp.simplify(num/den)
print("<E>(a) =", Eexp, " depends on c?", sp.diff(Eexp, c) == 0 and 'no' or 'yes')
amin = sp.solve(sp.diff(Eexp, a), a)[0]
print("minimizing shape: a =", amin, ", E =", sp.simplify(Eexp.subs(a, amin)))
ok = sp.simplify(sp.diff(Eexp, c)) == 0 and sp.simplify(amin - hb**2/(m*k*e**2)) == 0
print("PASS" if ok else "FAIL")
