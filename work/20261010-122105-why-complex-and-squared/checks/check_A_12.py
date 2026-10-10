# Claim: S_p = 2^{-1/p}[[1,1],[1,-1]]; second pass gives (2^{1-2/p}, 0) with "p-total 2^{p-2}.
# That equals 1 only when p = 2", table values; p=1 sign-free 1/2[[1,1],[1,1]] sends (1/2,-1/2) to 0;
# "2*(1/sqrt2)^p = 2^{1-p/2} (1.41 for p=1, 1 for p=2, 0.71 for p=3, 0.5 for p=4)".
import sympy as sp, numpy as np
p = sp.symbols('p', positive=True)
S = 2**(-1/p)*sp.Matrix([[1, 1], [1, -1]])
o1 = S*sp.Matrix([1, 0]); tot1 = sp.simplify(2*(2**(-1/p))**p)
o2 = sp.simplify(S*o1)
ok = sp.simplify(tot1 - 1) == 0 and sp.simplify(o2[0] - 2**(1-2/p)) == 0 and o2[1] == 0
tot2 = sp.simplify((2**(1-2/p))**p)
ok &= sp.simplify(tot2 - 2**(p-2)) == 0
ok &= sp.solve(sp.Eq(2**(p-2), 1), p) == [2]
claimed = {1: (0.500, 0.5, 0.5), 2: (0.707, 1, 1), 3: (0.794, 1.26, 2), 4: (0.841, 1.414, 4)}
for pv, (e, out, t) in claimed.items():
    E = 2**(-1/pv); O = 2**(1-2/pv); Tt = 2**(pv-2)
    good = abs(E-e) < 6e-4 and abs(O-out) < 6e-3 and abs(Tt-t) < 1e-12
    ok &= good; print(f'p={pv}: entry {E:.3f}, output {O:.3f}, p-total {Tt:g}  {good}')
N = sp.Matrix([[1, 1], [1, 1]])/2
ok &= N*sp.Matrix([sp.Rational(1, 2), -sp.Rational(1, 2)]) == sp.zeros(2, 1)
for pv, c in {1: 1.41, 2: 1, 3: 0.71, 4: 0.5}.items():
    v = 2*(1/np.sqrt(2))**pv; ok &= abs(v - c) < 0.006 and abs(v - 2**(1-pv/2)) < 1e-12
    print(f'2(1/rt2)^{pv} = {v:.4f}')
print('PASS' if ok else 'FAIL')
