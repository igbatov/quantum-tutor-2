# Claim: "(b) plates in: no stripes, the smooth two-one-slit-chances-added pattern" (d = 4a, far screen)
# Test the full one-slit pattern S(X) = sinc^2(pi X/4) beyond the plotted window -4..4.
import numpy as np
from scipy.signal import argrelextrema
X = np.linspace(-20, 20, 400001)
S = np.sinc(X/4)**2
mx = argrelextrema(S, np.greater)[0]; mn = argrelextrema(S, np.less)[0]
print("local maxima at X =", np.round(X[mx], 2), "heights", np.round(S[mx], 4))
print("minima (zeros) at X =", np.round(X[mn], 2), "values", np.round(S[mn], 6))
side = S[mx][np.argsort(-S[mx])][1]
print(f"first side band height = {side*100:.1f}% of centre")
# two-slit stripes absent: contrast of interference term with orthogonal tag = 0 exactly (see check_A_06)
ok = len(mx) == 1
print("PASS" if ok else "FAIL: no two-slit stripes, but the pattern is not a single smooth hump; one-slit side bands (4.7%) with dark zeros at X = +-4, +-8, ... lie outside the -4..4 window")
