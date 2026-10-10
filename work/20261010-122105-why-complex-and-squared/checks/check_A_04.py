# Claim: the table of z, (z+1)/2, P1, (z-1)/2, P2 at 0, 60, 90, 120, 180 degrees.
import numpy as np
table = {0: (1, 1, 1, 0, 0), 60: (0.5+0.866j, 0.75+0.433j, 0.75, -0.25+0.433j, 0.25),
         90: (1j, 0.5+0.5j, 0.5, -0.5+0.5j, 0.5), 120: (-0.5+0.866j, 0.25+0.433j, 0.25, -0.75+0.433j, 0.75),
         180: (-1, 0, 0, -1, 1)}
tol = 6e-4; ok = True
for d, (zc, ac, p1c, bc, p2c) in table.items():
    z = np.exp(1j*np.radians(d)); a = (z+1)/2; b = (z-1)/2
    p1, p2 = abs(a)**2, abs(b)**2
    good = abs(z-zc) < tol and abs(a-ac) < tol and abs(p1-p1c) < tol and abs(b-bc) < tol and abs(p2-p2c) < tol and abs(p1+p2-1) < 1e-12
    ok &= good
    print(f'{d:4d}: z={z:.3f} a={a:.3f} P1={p1:.4f} b={b:.3f} P2={p2:.4f} sum={p1+p2:.3f} {good}')
# partial sums written in table
ok &= abs(0.75**2 - 0.5625) < 1e-12 and abs((np.sqrt(3)/4)**2 - 0.1875) < 1e-12 and abs(0.25**2 - 0.0625) < 1e-12
print('PASS' if ok else 'FAIL')
