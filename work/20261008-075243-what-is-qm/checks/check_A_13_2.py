# Claim: "Electrons are sent so rarely that each has almost always landed before the next one leaves"
# Tonomura 1989-like numbers: 50 keV, ~1.5 m flight, <=1000 electrons/s (Poisson emission)
import numpy as np
from scipy.constants import m_e, e, c
gamma = 1 + 50e3*e/(m_e*c**2); v = c*np.sqrt(1-1/gamma**2); T = 1.5/v
for rate in (1e3, 1e4):
    p_next_during_flight = 1 - np.exp(-rate*T)
    print(f"rate {rate:.0e}/s: flight {T:.2e} s, mean gap {1/rate:.1e} s, P(next leaves before landing)={p_next_during_flight:.1e}")
ok = 1 - np.exp(-1e3*T) < 1e-3
# "almost always" (not "always") is right: Poisson emission gives a nonzero overlap chance
print("PASS" if ok and 1-np.exp(-1e3*T) > 0 else "FAIL")
