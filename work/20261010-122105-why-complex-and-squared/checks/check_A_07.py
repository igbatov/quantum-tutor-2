# Claim (model 2): "each splitter shrinks a hand by 1/sqrt2 ... |A1| = |A2| = 1/2";
# table: totals 1, 0.707 (squared 0.50), 0 at 0, 90, 180 deg; exit-1 amplitude (z+1)/2.
import numpy as np
A = (1/np.sqrt(2))**2
ok = abs(A - 0.5) < 1e-12
for d, L, L2 in [(0, 1, 1), (90, 0.707, 0.50), (180, 0, 0)]:
    tot = A*np.exp(1j*np.radians(d)) + A
    good = abs(abs(tot) - L) < 6e-4 and abs(abs(tot)**2 - L2) < 1e-12 and abs(tot - (np.exp(1j*np.radians(d))+1)/2) < 1e-12
    ok &= good
    print(d, 'total', round(abs(tot), 4), 'squared', round(abs(tot)**2, 4), good)
ok &= abs(np.sqrt(0.25+0.25) - 0.7071) < 1e-4
print('PASS' if ok else 'FAIL')
