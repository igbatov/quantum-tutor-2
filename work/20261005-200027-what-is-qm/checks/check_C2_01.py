# Claims: "tiny, heavy, positive nucleus with much lighter, negative electrons";
# "spiral into the nucleus in about a hundred-billionth of a second"
import numpy as np
from scipy.constants import physical_constants as pc, c, m_e, m_p
a0 = pc['Bohr radius'][0]; re = pc['classical electron radius'][0]
t = a0**3/(4*re**2*c)   # Larmor collapse time from r = a0 to 0 (nonrelativistic)
r_p = pc['proton rms charge radius'][0]
print(f"m_p/m_e = {m_p/m_e:.1f}; atom/nucleus size = a0/r_p = {a0/r_p:.0f}")
print(f"classical collapse time = {t:.3e} s (claim ~1e-11 s, 'about a hundred-billionth')")
ok = m_p/m_e > 1000 and a0/r_p > 1e4 and 0.3e-11 < t < 3e-11
print("PASS" if ok else "FAIL")
