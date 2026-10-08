# Claim (objective collapse): localizes "extremely rarely for one electron, so the stripes form as usual,
# but almost at once for the vast number of particles in the screen"
import numpy as np
from scipy.constants import m_e, m_n, e, m_e as me, c
lam_GRW = 1e-16      # s^-1 per nucleon (GRW 1986); Adler's proposal ~1e-8
for lam in (1e-16, 1e-8):
    lam_e = lam*m_e/m_n   # mass-proportional (CSL-style) rate for an electron
    # 50 keV electron over 1.5 m
    gamma = 1 + 50e3*e/(me*c**2); v = c*np.sqrt(1-1/gamma**2); t = 1.5/v
    p_e = lam_e*t
    print(f"lambda={lam:g}/s: electron collapse prob during flight ({t:.1e} s) = {p_e:.1e}")
    for Nn in (1e15, 1e18, 1e23):
        print(f"   detector region with {Nn:.0e} nucleons displaced: collapse time {1/(lam*Nn):.1e} s")
ok = lam_GRW*m_e/m_n*1e-8 < 1e-20 and 1/(lam_GRW*1e23) < 1e-6
print("PASS" if ok else "FAIL")
print("note: 'almost at once' requires a macroscopic number (>~1e20) of nucleons to be displaced by the detection at GRW's rate")
