# Claim: "a dust grain shows no stripes in practice because air and light record its position constantly"
import numpy as np
from scipy.constants import k, h, atomic_mass, pi
T, P = 300.0, 101325.0
r = 5e-6; rho = 1000.0; m = rho*4/3*pi*r**3
n = P/(k*T); m_air = 29*atomic_mass
vbar = np.sqrt(8*k*T/(pi*m_air)); sigma = pi*r**2
rate = n*sigma*vbar
lam_th_air = h/np.sqrt(2*pi*m_air*k*T)
print(f"10 um grain: air collisions {rate:.1e} per s; each resolves position to ~{lam_th_air:.1e} m")
print(f"-> superpositions separated by more than ~1e-10 m decohere in ~{1/rate:.0e} s")
# for comparison: its own de Broglie wavelength at thermal speed and resulting stripe spacing
v = np.sqrt(k*T/m); lam = h/(m*v)
print(f"grain thermal speed {v:.1e} m/s, de Broglie {lam:.1e} m, stripe spacing (d=1 mm, L=1 m): {lam*1/1e-3:.1e} m")
ok = 1/rate < 1e-12
print("PASS" if ok else "FAIL")
