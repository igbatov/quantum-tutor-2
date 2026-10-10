# "every interference effect, however many alternatives there are, is a sum of pair terms,
#  one for each pair of alternatives" ; check-yourself: four slits from singles and pairs alone.
import numpy as np, sympy as sp
rng = np.random.default_rng(3)
ok = True
for N in [2, 3, 4, 5, 8]:
    z = rng.normal(size=N) + 1j*rng.normal(size=N)
    interf = abs(z.sum())**2 - np.sum(abs(z)**2)
    terms = [2*np.real(z[i]*np.conj(z[j])) for i in range(N) for j in range(i+1, N)]
    pairs = sum(abs(z[i]+z[j])**2 for i in range(N) for j in range(i+1, N))
    frompairs = pairs - (N-2)*np.sum(abs(z)**2)
    print(f"N={N}: interference {interf:.6f} = sum of {len(terms)} pair terms {sum(terms):.6f}; "
          f"|sum|^2 {abs(z.sum())**2:.6f} from pairs and singles {frompairs:.6f}")
    ok &= abs(interf - sum(terms)) < 1e-10 and len(terms) == N*(N-1)//2 and abs(abs(z.sum())**2 - frompairs) < 1e-10
# symbolic, N = 4
xs = sp.symbols('x1:5', real=True); ys = sp.symbols('y1:5', real=True)
sq = lambda idx: sum(xs[i] for i in idx)**2 + sum(ys[i] for i in idx)**2
expr = sq(range(4)) - sum(sq((i, j)) for i in range(4) for j in range(i+1, 4)) + 2*sum(sq((i,)) for i in range(4))
print("four slits, symbolic: |A+B+C+D|^2 - pairs + 2 singles =", sp.expand(expr))
ok &= sp.expand(expr) == 0
print("PASS" if ok else "FAIL")
