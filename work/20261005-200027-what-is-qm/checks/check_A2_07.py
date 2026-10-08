# Figure/structure claims: dark stripes at X = +-0.5, +-1.5 with "curve 3 exactly zero" and P1 "about 0.95 ... and 0.62";
# also scan the full two-slit pattern for features the text does not mention.
import numpy as np
P1 = lambda X: np.sinc(X/4)**2
P2 = lambda X: 4*P1(X)*np.cos(np.pi*X)**2
for x in [0.5, 1.5]: print(f"X={x}: P1={P1(x):.4f}, both={P2(x):.1e}")
ok = abs(P1(0.5)-0.95) < 0.01 and abs(P1(1.5)-0.62) < 0.01 and P2(0.5) < 1e-25 and P2(1.5) < 1e-25
print("figure values:", "PASS" if ok else "FAIL")
for k in range(0, 9): print(f"bright-stripe position X={k}: both={P2(k):.4f}, 2*P1={2*P1(k):.4f}")
print("note: bright stripe at X=+-4 (and +-8) is missing (envelope zero); outer stripes beyond |X|=4 are <=19% of centre.")
