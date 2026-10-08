# Claim: classical orbiting electron "should spiral into the nucleus in roughly a hundred-billionth of a second"
import numpy as np
from scipy.constants import physical_constants, c
a0 = physical_constants['Bohr radius'][0]
re = physical_constants['classical electron radius'][0]
# Larmor-radiation collapse time from r=a0 to 0 (nonrelativistic): t = a0^3 / (4 re^2 c)
t = a0**3/(4*re**2*c)
print(f"collapse time = {t:.3e} s; claimed ~1e-11 s")
print("PASS" if 0.3e-11 < t < 3e-11 else "FAIL")
