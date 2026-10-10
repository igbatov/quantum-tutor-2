# Claim: "H(z,1)/sqrt2 = 1/2 (z+1, z-1)"; "P1 = cos^2(phi/2), P2 = sin^2(phi/2), P1+P2 = 1";
# "U = H P H = 1/2[[z+1,z-1],[z-1,z+1]]", "PH = 1/sqrt2[[z,z],[1,-1]]"; period 2pi = one wavelength;
# figure ticks 0..4pi = extra path 0..2 lambda; quarter wavelength -> 90 deg, half -> sign flip.
import sympy as sp
f = sp.symbols('phi', real=True)
z = sp.exp(sp.I*f)
H = sp.Matrix([[1, 1], [1, -1]])/sp.sqrt(2)
P = sp.Matrix([[z, 0], [0, 1]])
s1 = H*sp.Matrix([1, 0])
ok1 = sp.simplify(s1 - sp.Matrix([1, 1])/sp.sqrt(2)) == sp.zeros(2, 1)
out = H*P*s1
ok2 = sp.simplify(out - sp.Matrix([z+1, z-1])/2) == sp.zeros(2, 1)
c, s = sp.cos(f), sp.sin(f)
ok3 = sp.simplify((1+c)**2 + s**2 - (2+2*c)) == 0 and sp.simplify((c-1)**2 + s**2 - (2-2*c)) == 0
P1 = sp.simplify(sp.expand(out[0]*sp.conjugate(out[0])))
P2 = sp.simplify(sp.expand(out[1]*sp.conjugate(out[1])))
ok4 = sp.simplify(P1 - sp.cos(f/2)**2) == 0 and sp.simplify(P2 - sp.sin(f/2)**2) == 0
ok5 = sp.simplify(P1 + P2 - 1) == 0
ok6 = sp.simplify(P*H - sp.Matrix([[z, z], [1, -1]])/sp.sqrt(2)) == sp.zeros(2)
U = H*P*H
ok7 = sp.simplify(U - sp.Matrix([[z+1, z-1], [z-1, z+1]])/2) == sp.zeros(2)
ok8 = sp.simplify(U*U.H - sp.eye(2)) == sp.zeros(2)
ok9 = sp.simplify(P1.subs(f, f + 2*sp.pi) - P1) == 0 and sp.simplify(P1.subs(f, f + sp.pi) - P1) != 0
lam = sp.symbols('lambda', positive=True)
phase = lambda d: 2*sp.pi*d/lam
ok10 = [sp.simplify(phase(k*lam/2)) for k in range(5)] == [0, sp.pi, 2*sp.pi, 3*sp.pi, 4*sp.pi]
ok11 = sp.simplify(phase(lam/4)) == sp.pi/2 and sp.exp(sp.I*phase(lam/2)) == -1
# monotone sweep from 1 to 0 on [0, pi]
import numpy as np
ph = np.linspace(0, np.pi, 2001); p1 = np.cos(ph/2)**2
ok12 = np.all(np.diff(p1) < 0) and abs(p1[0]-1) < 1e-12 and abs(p1[-1]) < 1e-12
res = dict(H10=ok1, out=ok2, mod=ok3, P12=ok4, sum=ok5, PH=ok6, U=ok7, unitary=ok8, period=ok9, ticks=ok10, quarter=ok11, monotone=ok12)
print(res)
print('PASS' if all(res.values()) else 'FAIL')
