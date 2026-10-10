# Claims (Model 3): "-i Gamma would make |c1|^2 decay as e^{-2 Gamma t/hbar}"; the d|c1|^2/dt chain
# "= (2/hbar) Im(H12 c1bar c2)"; c2 rate "(1/i hbar)(H12bar c1 c2bar - H12 c1bar c2) = -(2/hbar) Im(...)";
# "H11 = H22 = 0, H12 = 1, H21 = 4 has the real energies +-2, yet under it |c1|^2 + |c2|^2 grows";
# ammonia: "c1 = cos(At/hbar), c2 = i sin(At/hbar)" solves; "A real c2 = sin(At/hbar) fails the first check".
import sympy as sp, numpy as np
from scipy.linalg import expm
t = sp.symbols('t', real=True); hb, G, A = sp.symbols('hbar Gamma A', positive=True)
H11, H22, hr, hi = sp.symbols('H11 H22 hr hi', real=True); h12 = hr + sp.I*hi
a1, b1, a2, b2 = sp.symbols('a1 b1 a2 b2', real=True)
c1, c2 = a1+sp.I*b1, a2+sp.I*b2
d1 = (H11*c1 + h12*c2)/(sp.I*hb); d2 = (sp.conjugate(h12)*c1 + H22*c2)/(sp.I*hb)
r1 = sp.expand(sp.conjugate(c1)*d1 + c1*sp.conjugate(d1)); r2 = sp.expand(sp.conjugate(c2)*d2 + c2*sp.conjugate(d2))
z = h12*sp.conjugate(c1)*c2
mid1 = (H11*c1*sp.conjugate(c1) - H11*c1*sp.conjugate(c1) + z - sp.conjugate(z))/(sp.I*hb)
ok = sp.simplify(r1 - mid1) == 0 and sp.simplify(r1 - 2/hb*sp.im(sp.expand(z))) == 0
ok &= sp.simplify(r2 - (sp.conjugate(z) - z)/(sp.I*hb)) == 0 and sp.simplify(r2 + 2/hb*sp.im(sp.expand(z))) == 0
ok &= sp.simplify(r1 + r2) == 0
cg = sp.exp(-sp.I*(H11 - sp.I*G)*t/hb)
ok &= sp.simplify(sp.expand(cg*sp.conjugate(cg)) - sp.exp(-2*G*t/hb)) == 0
# non-Hermitian counterexample
M = np.array([[0, 1], [4, 0]], complex); print("eigenvalues:", np.linalg.eigvals(M))
ok &= np.allclose(sorted(np.linalg.eigvals(M).real), [-2, 2]) and np.allclose(np.linalg.eigvals(M).imag, 0)
ts = np.linspace(0, 2*np.pi, 2001)
n1 = np.array([np.linalg.norm(expm(-1j*M*tt) @ [1, 0])**2 for tt in ts])
n2 = np.array([np.linalg.norm(expm(-1j*M*tt) @ [0, 1])**2 for tt in ts])
print(f"start level 1: norm in [{n1.min():.3f}, {n1.max():.3f}], = 1 + 3 sin^2(2t)? {np.allclose(n1, 1+3*np.sin(2*ts)**2)}")
print(f"start level 2: norm in [{n2.min():.3f}, {n2.max():.3f}]")
grows_claim = n2.max() > 1 + 1e-9 and np.all(np.diff(n1[:200]) >= -1e-12) and n1[-1] > 1.5
print("'grows' true as written (for every start, and keeps growing):", grows_claim)
# ammonia
a1t, a2t = sp.cos(A*t/hb), sp.I*sp.sin(A*t/hb)
ok &= sp.simplify(sp.I*hb*sp.diff(a1t, t) + A*a2t) == 0 and sp.simplify(sp.I*hb*sp.diff(a2t, t) + A*a1t) == 0
rc2 = sp.sin(A*t/hb); ok &= sp.simplify(sp.I*hb*sp.diff(a1t, t) + A*rc2) != 0
print("derivations, decay, counterexample energies, ammonia: PASS" if ok else "FAIL")
print("'yet under it |c1|^2+|c2|^2 grows': " + ("PASS" if grows_claim else "FAIL (it oscillates: 1 -> 4 -> 1 from level 1, 1 -> 1/4 -> 1 from level 2)"))
