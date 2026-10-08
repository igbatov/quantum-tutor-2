# Claim: "At the dark stripes, where with both slits open almost no electrons land
# (none in the ideal set-up), electrons now land. Opening a second slit took hits away."
# Also the Check-yourself question: a spot dark with both slits open -> cover one slit -> electrons land?
import numpy as np
from scipy.signal import argrelmin
X = np.linspace(-8, 8, 160001)
P1 = np.sinc(X/4)**2
Pb = 4*P1*np.cos(np.pi*X)**2
# 1) interference minima at half-integers: Pb = 0, P1 > 0
half = np.arange(-7.5, 8, 1.0)
P1h = np.sinc(half/4)**2; Pbh = 4*P1h*np.cos(np.pi*half)**2
print("half-integer dark stripes: max Pb =", Pbh.max(), " min P1 =", P1h.min().round(4))
# 2) every zero of P1 is also a zero of Pb (Pb = 4 P1 cos^2): X = +-4, +-8
for x0 in [4.0, 8.0]:
    print(f"X={x0}: P1={np.sinc(x0/4)**2:.2e}, Pb={4*np.sinc(x0/4)**2*np.cos(np.pi*x0)**2:.2e}")
# dark region around X=4 in both-slit pattern: max Pb in [3.5,4.5] vs central peak 4
m = (X > 3.5) & (X < 4.5)
print(f"max Pb in 3.5<X<4.5 = {Pb[m].max():.4f} (central peak 4; relative {Pb[m].max()/4:.2e})")
# where does opening the second slit ADD hits? Pb > P1  <=> 4cos^2 > 1
frac_more = np.mean(Pb > P1 + 1e-15)
print(f"fraction of screen (|X|<8) where both slits give MORE hits than one: {frac_more:.2f}")
# real set-up: 5% spread of speeds (wavelength) -> nonzero minimum at X=0.5
lams = np.linspace(0.95, 1.05, 201)
def Preal(x):
    return np.mean([4*np.sinc(x/lam/4)**2*np.cos(np.pi*x/lam)**2 for lam in lams])
print(f"real (5% speed spread): P_both(0.5)={Preal(0.5):.2e} vs P1(0.5)={np.sinc(0.125)**2:.3f}")
ok_near_centre = Pbh.max() < 1e-25 and P1h.min() > 0.01
universal = ok_near_centre and np.sinc(1.0)**2 > 1e-12  # fails: single-slit zeros are also dark with both
print("interference dark stripes (half-integers): PASS" if ok_near_centre else "FAIL")
print("FAIL (as a statement about every dark spot): at X=+-4, +-8 the spot is dark with both slits AND with one;"
      " there opening the second slit multiplies hits by 4cos^2=4 (0 -> 0 ideally).")
