# Claims: "Independent recorders multiply: three scatterings with overlap 0.7 each leave ~0.34";
# "average visibility is exp(-(mean number)(1-c)), still an exponential in pressure".
import numpy as np, sympy as sp
rng = np.random.default_rng(1)
def rec_states(c):
    # two normalized recorder states with real overlap c
    return np.array([1, 0.]), np.array([c, np.sqrt(1-c**2)])
cs = [0.7, 0.7, 0.7]
e0 = np.array([1.]); e1 = np.array([1.])
for c in cs:
    a, b = rec_states(c); e0 = np.kron(e0, a); e1 = np.kron(e1, b)
# particle (1/sqrt2)(|L>e0 + |R>e1); reduced coherence = <e0|e1>
coh = e0 @ e1
print(f"joint-state coherence after 3 recorders = {coh:.4f} ; 0.7^3 = {0.7**3:.4f}")
mu, cc, n = sp.symbols('mu c n', positive=True)
avg = sp.simplify(sp.summation(sp.exp(-mu)*mu**n/sp.factorial(n)*cc**n, (n, 0, sp.oo)))
print("Poisson average of c^n =", avg, "| equals exp(-mu(1-c)):", sp.simplify(avg - sp.exp(-mu*(1-cc))) == 0)
print("visibilities 0,1,2,3 events at 0.7:", [round(0.7**k, 3) for k in range(4)])
ok = abs(coh-0.343) < 1e-9 and sp.simplify(avg - sp.exp(-mu*(1-cc))) == 0 and round(0.7**3, 2) == 0.34
print("PASS" if ok else "FAIL")
