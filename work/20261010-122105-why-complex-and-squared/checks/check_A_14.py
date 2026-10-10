# Claim: "give each hand a new length equal to the square root of its old length ... call the fourth
# power of the new length the chance, and every count comes out the same; but renamed hands no longer
# add tip to tail".
import numpy as np
r = np.linspace(0, 1, 11); ok = np.allclose(np.sqrt(r)**4, r**2)
# two equal hands of old length 1/2 in the same direction: old rule total 1 -> chance 1
old = 0.5 + 0.5; new_each = np.sqrt(0.5); new_sum = 2*new_each
print('old-rule chance', old**2, '| renamed hands added tip to tail then ^4:', round(new_sum**4, 3))
ok &= abs(old**2 - 1) < 1e-12 and abs(new_sum**4 - 1) > 0.5
print('PASS' if ok else 'FAIL')
