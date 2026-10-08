# Claim: "only ... one half-wave, two, three, never two and a half" fit a string fixed at both ends
import numpy as np
L = 1.0
res = {n: np.sin(n*np.pi*L) for n in (1, 2, 3, 2.5)}
for n, v in res.items(): print(f"n={n}: y(x=L) = {v:.3e}")
ok = all(abs(res[n]) < 1e-12 for n in (1,2,3)) and abs(res[2.5]-1) < 1e-12
# general: sin(kL)=0 requires kL = n*pi -> L = n * (lambda/2)
print("PASS" if ok else "FAIL")
