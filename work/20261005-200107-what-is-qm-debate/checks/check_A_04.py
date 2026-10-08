# Claim: "wavelength ... shorter for faster electrons"; "electron's wavelength fixes its momentum (mass times velocity)"
import numpy as np
from scipy.constants import h, m_e, c
v = np.array([1e5, 1e6, 1e7, 1e8, 2.5e8])
gamma = 1/np.sqrt(1 - (v/c)**2)
lam_nr = h/(m_e*v); lam_rel = h/(gamma*m_e*v)
for vi, a, b in zip(v, lam_nr, lam_rel):
    print(f"v={vi:.1e} m/s  lambda(h/mv)={a:.3e} m  lambda(relativistic)={b:.3e} m")
ok = np.all(np.diff(lam_nr) < 0) and np.all(np.diff(lam_rel) < 0)
print("PASS" if ok else "FAIL", "(lambda = h/p decreases monotonically with speed; p = m v non-relativistically)")
