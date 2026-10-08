# Claims: gas atom "wavelength of tens of picometres" is "tens of thousands of times shorter
# than the micrometre or so between the paths"; with such wavelengths one collision's two outgoing
# states are "at right angles"; one glancing collision "barely deflects a heavy molecule" (C70);
# "a few millionths of a millibar, about a billionth of atmospheric pressure".
import numpy as np
from scipy.constants import h, k, atomic_mass as u
T = 300.0; dx = 1e-6
ok = True
for name, m in [("He", 4), ("Ar", 40), ("CH4", 16), ("Xe", 131)]:
    lam = h/np.sqrt(3*m*u*k*T)   # de Broglie at rms speed
    print(f"{name}: lambda = {lam*1e12:.0f} pm ; dx/lambda = {dx/lam:.1e}")
    ok &= 5e-12 < lam < 100e-12 and 1e4 < dx/lam < 1e6
# single-collision overlap for isotropic scattering: <exp(i q.dx)> averaged over in/out directions
rng = np.random.default_rng(3)
def overlap(kdx, n=400000):
    ki = rng.normal(size=(n, 3)); ki /= np.linalg.norm(ki, axis=1)[:, None]
    ko = rng.normal(size=(n, 3)); ko /= np.linalg.norm(ko, axis=1)[:, None]
    q = (ki-ko)[:, 0]*kdx; return abs(np.mean(np.exp(1j*q)))
kdx = 2*np.pi*dx/(h/np.sqrt(3*16*u*k*T))
print(f"overlap for k*dx={kdx:.1e}: {overlap(kdx):.4f} (MC noise ~1/sqrt(n)=0.0016); for k*dx=0.1: {overlap(0.1):.4f}")
ok &= overlap(kdx) < 0.01
# C70 deflection by a momentum kick just big enough to tag (q ~ h/dx), C70 at ~100-200 m/s
M = 70*12*u
for v in [100, 200]:
    ang = (h/dx)/(M*v); print(f"C70 at {v} m/s: deflection for q=h/dx = {ang:.1e} rad")
    ok &= ang < 1e-4
for p in [1e-6, 3e-6]:
    print(f"{p:.0e} mbar / 1013 mbar = {p/1013.25:.1e}")
ok &= 5e-10 < 3e-6/1013.25 < 5e-9
print("PASS" if ok else "FAIL")
