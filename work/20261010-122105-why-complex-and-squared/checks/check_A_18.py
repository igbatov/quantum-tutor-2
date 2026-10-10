# Claim (set-up): "tilting the plate lengthens the path inside it, so the arm's optical path ...
# grows smoothly with the tilt". Extra optical path of a plate (thickness d, index n) at tilt th:
# OPD = d (sqrt(n^2 - sin^2 th) - cos th). Also: real fringes of visibility V do not reach 0
# (min fraction (1-V)/2); the text attributes 100%->0% to the ideal case and quotes V = 98%.
import numpy as np
th = np.linspace(0, np.radians(80), 4001); ok = True
for n in (1.33, 1.5, 1.9):
    opd = np.sqrt(n**2 - np.sin(th)**2) - np.cos(th)
    ok &= np.all(np.diff(opd) > 0)
    print(f'n={n}: OPD/d from {opd[0]:.4f} (=n-1) rising to {opd[-1]:.4f}')
V = 0.98; print('V=0.98: exit-1 fraction ranges', (1-V)/2, 'to', (1+V)/2)
ok &= abs((1-V)/2 - 0.01) < 1e-12
print('PASS' if ok else 'FAIL')
