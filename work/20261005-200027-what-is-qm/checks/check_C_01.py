# Claim: "spiral into the nucleus in about a hundred-billionth of a second"
# Classical Larmor radiation collapse time from the Bohr radius: t = a0^3 / (4 r_e^2 c)
import numpy as np
from scipy.constants import physical_constants as pc, c
a0 = pc['Bohr radius'][0]; re = pc['classical electron radius'][0]
t = a0**3/(4*re**2*c)
print(f"collapse time = {t:.3e} s (claim ~1e-11 s)")
print("PASS" if 0.3e-11 < t < 3e-11 else "FAIL")
