# Claim: "r^2 = 1 and r = +1 or -1. With +1 every photon leaves by exit 1; with -1 ... exit 2.
# Nothing in between is available" (one real number per arm).
import sympy as sp, numpy as np
r = sp.symbols('r', real=True)
sols = sp.solve(sp.Eq(r**2, 1), r)
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
P1 = {}
for rv in sols:
    out = H @ np.diag([float(rv), 1]) @ H @ np.array([1, 0])
    P1[int(rv)] = (round(out[0]**2, 12), round(out[1]**2, 12))
ok = set(int(s) for s in sols) == {-1, 1} and P1[1] == (1.0, 0.0) and P1[-1] == (0.0, 1.0)
# also: any real r with arm count kept (|r|=1) and any real splitter phases give only these two patterns
print('solutions', sols, 'exit fractions', P1)
print('PASS' if ok else 'FAIL')
