# Claim: "crash into the proton in roughly 10^-11 seconds (a hundred-billionth of a second)"
# Classical Larmor in-spiral from r = a0: t = a0^3 / (4 r_e^2 c)
from scipy.constants import physical_constants as pc, c
import math
a0 = pc['Bohr radius'][0]; re = pc['classical electron radius'][0]
t = a0**3/(4*re**2*c)
print(f"t_collapse = {t:.3e} s; log10 = {math.log10(t):.2f}")
ok = abs(math.log10(t) - (-11)) < 0.5
print("hundred-billionth =", 1/100e9)
print("PASS" if ok and abs(1/100e9-1e-11)<1e-25 else "FAIL")
