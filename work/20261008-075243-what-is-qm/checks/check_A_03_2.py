# Claim: "At the dark stripes near the middle ... (none in the ideal set-up), electrons now land."
# + Check-yourself: "one of the dark stripes near the middle ... cover one slit"
import numpy as np
X = np.linspace(-8, 8, 160001)
P1 = np.sinc(X/4)**2; Pb = 4*P1*np.cos(np.pi*X)**2
# dark stripes near the middle = interference zeros inside the central one-slit band |X|<4
half = np.arange(-3.5, 4, 1.0)
P1h = np.sinc(half/4)**2; Pbh = 4*P1h*np.cos(np.pi*half)**2
print("near-middle dark stripes X=", half)
print("  Pb max =", Pbh.max(), "  P1 values =", P1h.round(4))
# are there any other zeros of Pb in |X|<4? (only half-integers)
from scipy.signal import argrelmin
idx = argrelmin(Pb)[0]; zeros = X[idx][(np.abs(X[idx])<3.9) & (Pb[idx] < 1e-6)]
print("all dark points of both-slit pattern with |X|<3.9:", np.round(zeros, 3))
# arrows in the figure at +-0.5, +-1.5
for x in (0.5, 1.5): print(f"X={x}: P1={np.sinc(x/4)**2:.3f}, Pb={4*np.sinc(x/4)**2*np.cos(np.pi*x)**2:.1e}")
# real set-up: 5% speed spread -> "almost no electrons"
lams = np.linspace(0.95, 1.05, 201)
Pr = np.mean([4*np.sinc(0.5/l/4)**2*np.cos(np.pi*0.5/l)**2 for l in lams])
print(f"5% speed spread: P_both(0.5)={Pr:.3e} (vs central 4) ; P1(0.5)={np.sinc(0.125)**2:.3f}")
ok = Pbh.max() < 1e-25 and P1h.min() > 0.01 and np.allclose(np.abs(zeros) % 1, 0.5, atol=1e-3) and Pr < 0.05
print("PASS" if ok else "FAIL")
