# Claim: "settles to the same size, about a ten-billionth of a metre across"
from scipy import constants as k
import numpy as np
a0 = k.physical_constants['Bohr radius'][0]
# ground state: <r> = 1.5 a0 ; diameter scale 2a0 ; most probable r = a0
print(f"a0={a0:.3e} m, 2a0={2*a0:.3e} m, 2<r>={3*a0:.3e} m")
ok = 0.5e-10 < 2*a0 < 2e-10
print("PASS" if ok else "FAIL")
