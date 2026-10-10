# Claims: p-table (1.307, 1.414, 0.845, 0.707, 0.750, 0.500); "2(1/sqrt2)^p = 2^{1-p/2}"; "any power below 2 overshoots,
# any power above 2 undershoots, worst at pi/4"; rabi-norms caption (p=1 rises to 1.414, p=3 dips 0.707, p=4 0.5,
# all meet at multiples of pi/2); how-they-relate caption: p = 1, 3, 4 curves "touch the motion only at its two ends";
# "p = 1 with hands that are never negative, is ordinary probability" (stochastic maps keep the sum and move it gradually).
import numpy as np, sympy as sp
from scipy.linalg import expm
P = sp.symbols('p', positive=True)
ok = sp.simplify(2*(1/sp.sqrt(2))**P - 2**(1-P/2)) == 0
th = np.array([0, np.pi/8, np.pi/4, 3*np.pi/8, np.pi/2])
tab = {1: [1,1.307,1.414,1.307,1], 2: [1]*5, 3: [1,0.845,0.707,0.845,1], 4: [1,0.750,0.500,0.750,1]}
for p, row in tab.items():
    val = np.cos(th)**p + np.sin(th)**p; print(p, np.round(val, 3)); ok &= np.allclose(np.round(val, 3), row)
g = np.linspace(1e-4, np.pi/2-1e-4, 20001)
for p in list(np.linspace(0.5, 1.99, 30)) + list(np.linspace(2.01, 12, 30)):
    s = np.cos(g)**p + np.sin(g)**p
    ok &= (np.all(s > 1) if p < 2 else np.all(s < 1)) and abs(g[np.argmax(np.abs(s-1))] - np.pi/4) < 1e-3
# rabi caption: integrate H = [[0,-1],[-1,0]] (A = hbar = 1) from level 1 over 0..2pi
ts = np.linspace(0, 2*np.pi, 1201); H = np.array([[0,-1],[-1,0]])
C = np.array([expm(-1j*H*t) @ [1,0] for t in ts])
ok &= np.allclose(np.abs(C[:,0])**2, np.cos(ts)**2) and np.allclose(np.abs(C[:,1])**2, np.sin(ts)**2)
for p, ext in [(1, 1.414), (3, 0.707), (4, 0.5)]:
    s = (np.abs(C)**p).sum(1); e = s.max() if p == 1 else s.min(); print("p", p, "extreme", round(e, 3)); ok &= abs(e-ext) < 1e-3
    ones = ts[np.abs(s-1) < 1e-6]; ok &= np.allclose(np.round(ones/(np.pi/2)), ones/(np.pi/2), atol=1e-2)
# how-they-relate: cos^p + sin^p = 1 on [0, pi/2] only at the ends for p != 2
for p in [1, 3, 4]:
    s = np.cos(g)**p + np.sin(g)**p; ok &= np.all(s > 1) if p < 2 else np.all(s < 1)   # strictly off the circle inside (0, pi/2)
# ordinary probability: a stochastic generator Q (columns sum to 0, off-diagonal >= 0) keeps sum p_k for p >= 0
Q = np.array([[-0.3, 0.5], [0.3, -0.5]]); q = expm(Q*1.7) @ [1, 0]
print("stochastic evolution:", q, "sum", q.sum()); ok &= abs(q.sum()-1) < 1e-12 and np.all(q >= 0) and 0 < q[1] < 1
print("PASS" if ok else "FAIL")
