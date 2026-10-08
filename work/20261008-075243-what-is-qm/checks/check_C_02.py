# Claim: "every line shifted by the same fraction by the source's motion or the universe's expansion"
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from hcommon_C import *
import numpy as np
lines = np.array([vac_nm(n,2) for n in (3,4,5,6)])
ok = True
for z in (0.001, 0.1, 1.0, 3.0):           # cosmological: 1+z = lam_obs/lam_emit for all lines
    obs = lines*(1+z); frac = (obs-lines)/lines
    ok &= np.allclose(frac, z, rtol=1e-12)
beta = 0.01                                 # relativistic Doppler, radial recession
D = np.sqrt((1+beta)/(1-beta)); frac = (lines*D-lines)/lines
ok &= np.allclose(frac, D-1, rtol=1e-12)
print("fractional shifts equal for all lines (z and Doppler):", ok, "Doppler frac", D-1)
print("PASS" if ok else "FAIL")
