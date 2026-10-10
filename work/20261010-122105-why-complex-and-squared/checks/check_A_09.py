# Claim: "a neutron's spin turned through 360 deg reverses the sign ... only 720 deg restores it".
import numpy as np
from scipy.linalg import expm
sz = np.array([[1, 0], [0, -1]]); sx = np.array([[0, 1], [1, 0]])
ok = True
for s in (sz, sx):
    R = lambda th: expm(-1j*th*s/2)
    ok &= np.allclose(R(2*np.pi), -np.eye(2)) and np.allclose(R(4*np.pi), np.eye(2))
print('R(2pi) = -1, R(4pi) = +1:', ok)
print('PASS' if ok else 'FAIL')
