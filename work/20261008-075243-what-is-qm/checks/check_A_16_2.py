# Claim: dust grain "wavelength is so tiny that its stripes would be far too fine to resolve",
# and "air and light constantly record its position"
import numpy as np
from scipy.constants import k, h, atomic_mass, pi
T = 300.0
for r in (0.5e-6, 5e-6):
    m = 1000*4/3*pi*r**3; v = np.sqrt(k*T/m); lam = h/(m*v)
    spacing = lam*1.0/1e-3      # d=1 mm, L=1 m
    print(f"radius {r*1e6:.1f} um: m={m:.1e} kg, v_th={v:.1e} m/s, lambda={lam:.1e} m, stripe spacing {spacing:.1e} m (proton ~1e-15 m)")
# even at 1 mm/s, 1 um grain
m = 1000*4/3*pi*(0.5e-6)**3; lam = h/(m*1e-3); print(f"1 um grain at 1 mm/s: lambda={lam:.1e} m, spacing {lam/1e-3:.1e} m")
# decoherence by air (as in check_A_11)
r = 5e-6; n = 101325/(k*T); m_air = 29*atomic_mass; rate = n*pi*r**2*np.sqrt(8*k*T/(pi*m_air))
print(f"air collisions on 10 um grain: {rate:.1e}/s")
ok = spacing < 1e-10 and rate > 1e12
print("PASS" if ok else "FAIL")
