# Claim: one slit gives "a wide bright band ... much fainter bands further out", "no fine stripes";
# figure numbers: P1 ~0.95 at |X|=0.5, 0.62 at 1.5, side band peak ~0.05 near |X|=5.7.
# Also verify that P(X) ~ cos^2(pi X) sinc^2(pi X/4) is the Fraunhofer pattern for d = 4a.
import numpy as np
from scipy.optimize import minimize_scalar
a, d = 1.0, 4.0
# Fraunhofer: amplitude at transverse spatial freq q = integral over apertures of exp(-i q y)
# with X in units of stripe spacing: q*d = 2 pi X
X = np.linspace(-8, 8, 4001)
q = 2*np.pi*X/d
y1 = np.linspace(-d/2-a/2, -d/2+a/2, 2001); y2 = y1 + d
def amp(ys):
    return np.trapezoid(np.exp(-1j*np.outer(q, ys)), ys, axis=1)
A1 = amp(y1); A2 = amp(y2)
P1num = np.abs(A1)**2/np.abs(A1[2000])**2
Pbnum = np.abs(A1+A2)**2/np.abs(A1[2000])**2
P1 = np.sinc(X/4)**2           # np.sinc(x)=sin(pi x)/(pi x)
Pb = 4*P1*np.cos(np.pi*X)**2
err1 = np.max(abs(P1num-P1)); errb = np.max(abs(Pbnum-Pb))
print(f"max |numeric - formula|: one slit {err1:.2e}, both {errb:.2e}")
v05 = np.sinc(0.5/4)**2; v15 = np.sinc(1.5/4)**2
r = minimize_scalar(lambda x: -np.sinc(x/4)**2, bounds=(4.5, 7.5), method='bounded')
print(f"P1(0.5)={v05:.4f}, P1(1.5)={v15:.4f}, side-band peak {-r.fun:.4f} at X={r.x:.3f}")
# one-slit pattern: central band width (zero to zero) = 8 stripe spacings; side bands < 5% of centre
# 'no fine stripes': count local maxima of P1 in |X|<8 (should be 1 central + 1 each side, spaced ~4+ units)
from scipy.signal import argrelmax
mx = argrelmax(P1)[0]
print("one-slit local maxima at X =", np.round(X[mx], 2), "values", np.round(P1[mx], 4))
ok = (err1 < 1e-3 and errb < 4e-3 and abs(v05-0.95) < 0.01 and abs(v15-0.62) < 0.01
      and abs(-r.fun-0.05) < 0.005 and abs(r.x-5.7) < 0.05 and np.all(P1[mx][abs(X[mx])>1] < 0.05))
print("PASS" if ok else "FAIL")
