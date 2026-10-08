# Claim: "Big objects obey them too, but their energy steps are far too small to notice"
# Check: 1 g bead in a 1 cm box, and a 1 m pendulum: quantum steps vs thermal energy kT at 300 K.
import numpy as np
from scipy.constants import hbar, h, k, g, pi
m, L = 1e-3, 1e-2
E1 = pi**2*hbar**2/(2*m*L**2); step = 3*E1
pend = hbar*np.sqrt(g/1.0)
kT = k*300
print(f"bead box E2-E1 = {step:.2e} J, pendulum hbar*omega = {pend:.2e} J, kT = {kT:.2e} J")
print(f"ratios: {step/kT:.1e}, {pend/kT:.1e}")
print("PASS" if step/kT < 1e-20 and pend/kT < 1e-10 else "FAIL")
