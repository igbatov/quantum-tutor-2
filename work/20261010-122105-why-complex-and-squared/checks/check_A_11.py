# Claim (Banach 1932, Lamperti 1958): "for any p with 1 <= p < inf and p != 2, the only linear maps
# that keep the p-total of every vector are relabellings ... none moves it gradually. For p = 2 ...
# unitary ... include gradual mixers". Also figure caption: rotated points (cos t, sin t) leave the
# diamond (p=1) and the p=4 curve except at the two ends.
# Numerical test at 2x2 (complex): force M(1,0) to put fraction t of the p-total at exit 2 and
# minimise the worst violation of p-total preservation over all unit vectors. Also p=0.5 (outside
# the stated theorem but inside "power p>0").
import numpy as np
from scipy.optimize import differential_evolution
ps_ = np.linspace(0.02, np.pi/2-0.02, 25); th = np.linspace(0, 2*np.pi, 13)[:-1]
PS, TH = np.meshgrid(ps_, th)
def worst(par, p, t):
    c1 = np.array([(1-t)**(1/p), t**(1/p)])
    c2 = np.array([par[0]+1j*par[1], par[2]+1j*par[3]])
    a = np.cos(PS)**(2/p); b = np.sin(PS)**(2/p)*np.exp(1j*TH)
    o1 = c1[0]*a + c2[0]*b; o2 = c1[1]*a + c2[1]*b
    dev = abs(abs(o1)**p + abs(o2)**p - 1)
    # also second basis vector alone
    dev0 = abs(abs(c2[0])**p + abs(c2[1])**p - 1)
    return max(dev.max(), dev0)
ok = True
for t in (0.5, 0.1):
    for p in (0.5, 1, 1.5, 2, 3, 4):
        r = differential_evolution(worst, [(-2, 2)]*4, args=(p, t), seed=3, tol=1e-12, maxiter=600, polish=True)
        verdict = (r.fun < 1e-6) if p == 2 else (r.fun > 1e-2)
        ok &= verdict
        print(f't={t} p={p}: smallest worst-case p-total error = {r.fun:.3e}  {"(mixer exists)" if r.fun < 1e-6 else "(no lossless mixer)"}')
# relabellings keep every p-total
rng = np.random.default_rng(0)
for p in (1, 3, 4):
    G = np.array([[0, np.exp(0.7j)], [-1, 0]])
    v = rng.normal(size=2)+1j*rng.normal(size=2)
    ok &= abs(np.sum(abs(G@v)**p) - np.sum(abs(v)**p)) < 1e-12
# figure caption: rotated points
for p in (1, 4):
    for d in (15, 30, 45, 60, 75):
        tt = np.radians(d); tot = abs(np.cos(tt))**p + abs(np.sin(tt))**p
        ok &= (tot > 1) if p == 1 else (tot < 1)
    ok &= abs(np.cos(0)**p + np.sin(0)**p - 1) < 1e-12 and abs(abs(np.cos(np.pi/2))**p + 1 - 1) < 1e-12
vals = {p: 2*(np.sqrt(0.5))**p for p in (1, 2, 4)}
print('45 deg p-totals:', {p: round(v, 3) for p, v in vals.items()})
ok &= abs(vals[1]-1.41) < 0.005 and abs(vals[2]-1) < 1e-12 and abs(vals[4]-0.5) < 1e-12
print('PASS' if ok else 'FAIL')
