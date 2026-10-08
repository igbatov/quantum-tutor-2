# Claim: "in which the lowest state has no orbiting at all" (L=0 in hydrogen ground state)
# Claim (pilot-wave): "in hydrogen's lowest state it sits still, ... energy of motion being here the energy of the wave's push"
import sympy as sp
r, th, ph = sp.symbols('r theta phi', positive=True)
a, hb, m = sp.symbols('a hbar m', positive=True)
psi = sp.exp(-r/a)/sp.sqrt(sp.pi*a**3)
# L^2 psi = -hbar^2 [ (1/sin) d/dth(sin dpsi/dth) + 1/sin^2 d2psi/dph2 ]
L2 = -hb**2*(sp.diff(sp.sin(th)*sp.diff(psi,th),th)/sp.sin(th) + sp.diff(psi,ph,2)/sp.sin(th)**2)
Lz = -sp.I*hb*sp.diff(psi, ph)
print("L^2 psi =", sp.simplify(L2), "; Lz psi =", sp.simplify(Lz))
ok1 = sp.simplify(L2) == 0 and sp.simplify(Lz) == 0
# Bohmian velocity v = (hbar/m) Im(grad psi / psi): psi real and nodeless -> phase constant -> v = 0
S = sp.arg(psi)
vel = [sp.diff(S, r), sp.diff(S, th), sp.diff(S, ph)]
print("phase S =", sp.simplify(S), "grad S =", [sp.simplify(v) for v in vel])
ok2 = all(sp.simplify(v) == 0 for v in vel)
# quantum potential Q = -hbar^2/(2m) lap(R)/R ; with a = hbar^2/(m k), V = -k/r
kk = sp.symbols('k', positive=True)
R = psi
lap = sp.diff(r**2*sp.diff(R, r), r)/r**2
Q = sp.simplify((-hb**2/(2*m)*lap/R).subs(a, hb**2/(m*kk)))
E = -m*kk**2/(2*hb**2)
V = -kk/r
print("Q(r) =", Q, "; Q + V - E =", sp.simplify(Q+V-E))
ok3 = sp.simplify(Q+V-E) == 0
rho = (R**2).subs(a, hb**2/(m*kk))
expQ = sp.integrate(Q*rho*4*sp.pi*r**2, (r, 0, sp.oo))
Tpsi = -hb**2/(2*m)*lap.subs(a, hb**2/(m*kk))
expT = sp.integrate((Tpsi*R.subs(a, hb**2/(m*kk)))*4*sp.pi*r**2, (r, 0, sp.oo))
print("<Q> =", sp.simplify(expQ), " <T> =", sp.simplify(expT), " -E =", sp.simplify(-E))
ok4 = sp.simplify(expQ-expT) == 0 and sp.simplify(expT+E) == 0
print("PASS" if (ok1 and ok2 and ok3 and ok4) else "FAIL")
