# Claim: "Now close one slit. The stripes vanish, leaving one broad hump."
# Full single-slit (Fraunhofer) model P1(X) = sinc^2(X/4), slit width = stripe-spacing setup (d = 4a),
# checked over a wide range |X| <= 40, not just the plotted window.
import numpy as np
from scipy.optimize import brentq, minimize_scalar
P1 = lambda X: np.sinc(X/4)**2
# zeros of P1 (dark bands of the single slit)
zeros = [4*k for k in range(1, 6)]
print("P1 at X=4k:", [float(P1(z)) for z in zeros])
# side-band maxima: tan(u)=u with u = pi X/4
peaks = []
for k in range(1, 5):
    res = minimize_scalar(lambda X: -P1(X), bounds=(4*k+0.01, 4*k+3.99), method="bounded")
    peaks.append((res.x, P1(res.x)))
for x, p in peaks: print(f"side band peak at X={x:.3f}: P1={p:.4f} ({100*p:.2f}% of central peak)")
# count local maxima over |X|<=40
X = np.linspace(-40, 40, 400001); y = P1(X)
nmax = np.sum((y[1:-1] > y[:-2]) & (y[1:-1] > y[2:]))
print("number of local maxima of one-slit pattern on |X|<=40:", nmax)
# fine stripes (period 1) gone? check no zeros of P1 in |X|<4
print("min of P1 on |X|<3.9:", y[np.abs(X) < 3.9].min())
one_hump = (nmax == 1)
print("Claim 'one broad hump' (single maximum, no other bands):", "PASS" if one_hump else "FAIL")
print("Claim 'fine two-slit stripes (period 1) vanish': PASS (P1 has no zeros for |X|<4; its dark bands are 4x farther apart)")
print("Overall for sentence as written: FAIL - central band plus fainter side bands (first ~4.7% of peak) separated by dark zeros at X=+-4,+-8,...")
