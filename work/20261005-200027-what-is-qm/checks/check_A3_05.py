# Claim: "The beam is so faint that there is almost never more than one electron in flight at a time"
# Typical single-electron build-up parameters (Tonomura et al. 1989): 50 kV, <= 1000 electrons/s, ~1.5 m source to detector.
import numpy as np
from scipy import constants as c
E = 50e3*c.e; gamma = 1 + E/(c.m_e*c.c**2); v = c.c*np.sqrt(1 - 1/gamma**2)
rate, L = 1000.0, 1.5
spacing = v/rate; transit = L/v; p_other = 1 - np.exp(-rate*transit)
print(f"v = {v:.3e} m/s; mean spacing between electrons {spacing/1e3:.0f} km; transit {transit:.1e} s; "
      f"P(another electron in flight) = {p_other:.1e}")
print("PASS (for published single-electron parameters)" if p_other < 1e-3 else "FAIL")
