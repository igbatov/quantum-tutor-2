# Claim: "the electrons missing from the dark stripes turn up in the bright ones"
# (total chance with both slits = total with which-slit record; interference only redistributes)
import numpy as np
from scipy import integrate
P1 = lambda X: np.sinc(X/4)**2
both = lambda X: 4*P1(X)*np.cos(np.pi*X)**2
rec = lambda X: 2*P1(X)
L = 4000.0
Ib = integrate.quad(both, -L, L, limit=20000)[0]
Ir = integrate.quad(rec, -L, L, limit=20000)[0]
print(f"integral both = {Ib:.5f}, integral record = {Ir:.5f}, rel diff = {abs(Ib-Ir)/Ir:.2e}")
# exact: int sinc^2(X/4) cos(2 pi X) dX = 0 since FT of sinc^2 is a triangle of half-width 1/4 < 1
print("PASS" if abs(Ib-Ir)/Ir < 1e-3 else "FAIL")
# also: classical "one slit or other" can only add: P1 + P1 >= P1 everywhere
X = np.linspace(-6, 6, 10001)
print("classical sum >= one slit everywhere:", np.all(rec(X) >= P1(X)))
