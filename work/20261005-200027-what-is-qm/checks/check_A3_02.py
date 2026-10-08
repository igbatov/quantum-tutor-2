# Claims: "first dark stripe beside the centre ... 95% as often as at the wide band's peak; with both open, almost never"
# "opening the second slit made some spots almost unreachable"; caption "falls to zero in this ideal calculation,
# and to nearly zero in real experiments, though one slit alone gives 95% or 62%"; "(completely in an ideal set-up, almost completely in a real one)"
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
P1 = lambda X: np.sinc(X/4)**2
P2 = lambda X, r=1.0: P1(X)*abs(1 + r*np.exp(2j*np.pi*X))**2
x0 = brentq(lambda x: np.cos(np.pi*x), 0.1, 0.9)            # first zero of two-slit pattern beside centre
print(f"first dark stripe at X={x0:.4f}; P1 there = {P1(x0):.4f}; P1 at 2nd dark stripe = {P1(1.5):.4f}")
print(f"ideal two-slit value there: {P2(x0):.1e}")
real = [quad(lambda x: P2(x), 0.5-0.05, 0.55)[0]/quad(P1, 0.45, 0.55)[0], P2(0.5, 0.9)/P1(0.5), 2*(1-0.99)]
print("realistic (spot 0.1 wide, amplitude ratio 0.9, visibility 0.99): both-open / one-slit =", np.round(real, 4))
ok = abs(P1(x0)-0.95) < 0.006 and abs(P1(1.5)-0.62) < 0.006  # tolerance: rounding to 2 digits and P2(x0) < 1e-12 and max(real) < 0.05 and min(real) > 0
print("95% / 62%; zero ideally, nearly zero (not zero) realistically -> 'almost never/almost unreachable':", "PASS" if ok else "FAIL")
