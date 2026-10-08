# Claims (decoherence): "overlap ... is the product of all the individual overlaps";
# "overlap of 0.9 each, fifty of them leave stripes about half a per cent strong";
# figure: "on a log scale the fall is a straight line"; Hornberger: stripe strength "fell
# exponentially with the pressure" if each collision writes a near-perfect tag.
import numpy as np
rng = np.random.default_rng(2)
# product of overlaps: tensor product of N two-state taggers
N = 6; ps = rng.uniform(0.3, 0.95, N); L = np.array([1.0]); R = np.array([1.0])
for p in ps:
    th = np.arccos(p); L = np.kron(L, [1, 0]); R = np.kron(R, [np.cos(th), np.sin(th)])
print("joint overlap", L@R, " product", np.prod(ps))
v50 = 0.9**50; print(f"0.9^50 = {v50:.5f}")
n = np.arange(61); y = np.log10(0.9**n); slope = np.diff(y)
print("log10 slope constant:", np.allclose(slope, slope[0]))
# Poisson number of collisions, mean proportional to pressure, each perfect tag (overlap 0):
lam = np.linspace(0, 5, 6); V = np.exp(-lam)   # <0^N>_Poisson = P(N=0) = e^-lam
mc = [np.mean(0.0**rng.poisson(l, 200000)) for l in lam]
print("Poisson MC:", np.round(mc, 4), " exp(-lam):", np.round(V, 4))
ok = abs(L@R-np.prod(ps)) < 1e-12 and 0.004 < v50 < 0.006 and np.allclose(slope, slope[0]) and np.allclose(mc, V, atol=3e-3)
print("PASS" if ok else "FAIL")
