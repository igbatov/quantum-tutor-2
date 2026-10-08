# Claim: "The ways through one slit interfere with each other too ... add up to a large total near
# the middle ... cancel much more farther out: completely at the dark gaps, partly in the much fainter side bands"
# Check: within-one-slit sum S(X) = (1/N) sum_k exp(i phi_k); cancellation measure |S| (1 = no cancellation).
import numpy as np
from scipy.optimize import minimize_scalar
a, N = 0.25, 4000
ys = 0.5 + a*((np.arange(N) + 0.5)/N - 0.5)          # right slit, offset d/2 = 0.5 (sign of offset irrelevant to |S|)
S = lambda X: np.exp(-2j*np.pi*X*ys).sum()/N
I = lambda X: abs(S(X))**2
print(f"centre X=0: |S| = {abs(S(0)):.4f} (all ways in phase, no cancellation), I = {I(0):.4f}")
gaps = [4, 8, 12]; gv = [I(g) for g in gaps]
print("dark gaps X=4,8,12: I =", ["%.1e" % v for v in gv])
peaks = [minimize_scalar(lambda X: -I(X), bounds=(lo, lo+4), method='bounded').x for lo in (4, 8, 12)]
pv = [I(p) for p in peaks]
print("side-band peaks at X =", np.round(peaks, 2), "I/I(0) =", np.round(pv, 4), "|S| =", np.round(np.sqrt(pv), 3))
# continuum check: |S| = |sinc(X/4)|
Xs = np.linspace(-14, 14, 2801); err = max(abs(abs(S(v)) - abs(np.sinc(v/4))) for v in Xs[::10])
print(f"max | |S| - |sinc(X/4)| | = {err:.1e}")
# central band: I > side bands everywhere in |X|<4 except near the gap edges; fraction of hits in central band
xf = np.linspace(-400, 400, 800001); p = np.sinc(xf/4)**2; frac = p[np.abs(xf) < 4].sum()/p.sum()
print(f"fraction of one-slit hits in central band |X|<4: {frac:.3f}")
# envelope of |S| decreases going out: maxima of |S| in successive lobes
lobe_max = [1.0] + list(np.sqrt(pv))
ok = (abs(S(0)) > 0.9999 and max(gv) < 1e-6 and 0.04 < pv[0] < 0.06
      and all(0 < v < 1 for v in np.sqrt(pv)) and all(np.diff(lobe_max) < 0) and err < 1e-4)
print("large total at centre, zero at gaps, partial (|S| 0.22, 0.13, 0.09) in side bands, decreasing outwards:", "PASS" if ok else "FAIL")
