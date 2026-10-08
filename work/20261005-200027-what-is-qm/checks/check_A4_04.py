# Claim: "With a reliable record, you add the two slits' chances instead of their combined amplitudes,
# so their contributions no longer cancel each other ... exactly the two one-slit patterns added together"
# Check: |psiL|^2 + |psiR|^2 = 2 P1 (dashed curve); no cross-slit cancellation (no narrow stripes), while
# within-slit zeros at X=+-4 remain (consistent with "two one-slit patterns", not "nothing cancels").
import numpy as np
d, a, N = 1.0, 0.25, 2000
X = np.linspace(-14, 14, 5601)
w = lambda c: c + a*((np.arange(N)+0.5)/N - 0.5)
amp = lambda ys: np.exp(-2j*np.pi*np.outer(X, ys)).sum(axis=1)/N
pL, pR = abs(amp(w(-.5)))**2, abs(amp(w(.5)))**2
P1 = np.sinc(X/4)**2
e = np.max(abs(pL + pR - 2*P1)); print(f"max| |psiL|^2+|psiR|^2 - 2 P1 | = {e:.1e}")
inner = np.abs(X) < 3.5; dips = np.sum((np.diff(np.sign(np.diff((pL+pR)[inner]))) > 0))
print("local minima of which-slit pattern inside |X|<3.5 (narrow stripes):", dips)
print("which-slit pattern at X=4 (within-slit gap):", f"{(pL+pR)[np.argmin(abs(X-4))]:.1e}")
print("PASS" if e < 1e-5 and dips == 0 else "FAIL")
