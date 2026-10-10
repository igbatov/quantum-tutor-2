# Claim: "three-way interference which the square rule forbids when the slits' amplitudes simply add"
# Sorkin's I3 = P_ABC - P_AB - P_AC - P_BC + P_A + P_B + P_C (P_empty = 0).
import sympy as sp, numpy as np
a, b, c = sp.symbols('a b c')
P = lambda z: z*sp.conjugate(z)
I3 = sp.expand(P(a+b+c) - P(a+b) - P(a+c) - P(b+c) + P(a) + P(b) + P(c))
print("I3 with square rule, additive complex amplitudes:", I3)
ok = I3 == 0
rng = np.random.default_rng(4)
for p in (1, 1.5, 3, 4):
    z = rng.normal(size=(1000, 3)) + 1j*rng.normal(size=(1000, 3))
    Pp = lambda w: np.abs(w)**p
    i3 = Pp(z.sum(1)) - Pp(z[:, 0]+z[:, 1]) - Pp(z[:, 0]+z[:, 2]) - Pp(z[:, 1]+z[:, 2]) + Pp(z).sum(1)
    print(f"p={p}: max |I3| = {np.max(np.abs(i3)):.2f} (nonzero)"); ok &= np.max(np.abs(i3)) > 1e-2
print("PASS" if ok else "FAIL")
