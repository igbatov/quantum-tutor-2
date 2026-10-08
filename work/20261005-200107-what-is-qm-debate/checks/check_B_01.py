# Claim: "spiral into the nucleus in about a hundred-billionth of a second"
# Also: "As it fell it would circle ever faster" (orbital frequency rises as r shrinks)
# Classical Larmor collapse time from Bohr radius: t = a0^3 / (4 r_e^2 c)
import numpy as np
from scipy import constants as C
a0 = C.physical_constants['Bohr radius'][0]
re = C.physical_constants['classical electron radius'][0]
t = a0**3/(4*re**2*C.c)
print(f"collapse time = {t:.3e} s (claim ~1e-11 s)")
ok1 = 0.3e-11 < t < 3e-11
# orbital frequency omega = sqrt(k e^2/(m r^3)) decreasing in r
k = 1/(4*np.pi*C.epsilon_0)
r = np.linspace(a0, a0/100, 50)
w = np.sqrt(k*C.e**2/(C.m_e*r**3))
ok2 = np.all(np.diff(w) > 0)
print(f"omega at a0 = {w[0]:.3e} rad/s, at a0/100 = {w[-1]:.3e} rad/s; monotonic increase: {ok2}")
print("PASS" if ok1 and ok2 else "FAIL")
