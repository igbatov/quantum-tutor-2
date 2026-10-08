# Claim: "Pre-quantum physics predicted ... electrons spiralling in within about a hundred-billionth of a second"
# Classical Larmor collapse of hydrogen from r=a0: t = a0^3 / (4 r_e^2 c)
from scipy.constants import c, physical_constants
a0 = physical_constants['Bohr radius'][0]; re = physical_constants['classical electron radius'][0]
t = a0**3/(4*re**2*c)
print(f"classical collapse time = {t:.3e} s  (claim: ~1e-11 s)")
import math
ok = abs(math.log10(t) - (-11)) < 0.5
print("PASS" if ok else "FAIL")
