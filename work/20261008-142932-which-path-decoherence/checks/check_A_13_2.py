# Claims: gas atom "wavelength of tens of picometres is tens of thousands of times shorter than the
# path separation" (~1 um); "one glancing collision, which barely deflects a heavy molecule, is a
# near-perfect tag"; "a few millionths of a millibar, about a billionth of atmospheric pressure".
import numpy as np
from scipy.constants import h, k, atomic_mass as u
T = 300.0; dx = 1e-6; ok = True
for name, m in [("He", 4), ("CH4", 16), ("Ar", 40), ("Xe", 131)]:
    lam = h/np.sqrt(3*m*u*k*T); print(f"{name}: {lam*1e12:.0f} pm, dx/lambda = {dx/lam:.1e}")
    ok &= 10e-12 <= lam < 100e-12 and 1e4 <= dx/lam < 1e5
rng = np.random.default_rng(3)
def overlap(kdx, n=400000):
    a = rng.normal(size=(n, 3)); a /= np.linalg.norm(a, axis=1)[:, None]
    b = rng.normal(size=(n, 3)); b /= np.linalg.norm(b, axis=1)[:, None]
    return abs(np.mean(np.exp(1j*(a-b)[:, 0]*kdx)))
kdx = 2*np.pi*dx/(h/np.sqrt(3*40*u*k*T)); o = overlap(kdx)
print(f"isotropic-scattering overlap at k*dx = {kdx:.1e}: {o:.4f} (MC noise ~0.0016)"); ok &= o < 0.01
M = 70*12*u
for v in [100, 200]:
    print(f"C70 at {v} m/s, kick h/dx: deflection {(h/dx)/(M*v):.1e} rad"); ok &= (h/dx)/(M*v) < 1e-4
# a full Ar momentum transfer (head-on) for comparison
pAr = np.sqrt(3*40*u*k*T); print(f"even a head-on Ar kick (2p = {2*pAr:.1e}) deflects C70 at 150 m/s by {2*pAr/(M*150):.1e} rad")
for p in [1e-6, 3e-6, 5e-6]: print(f"{p:.0e} mbar = {p/1013.25:.1e} atm")
ok &= 5e-10 < 3e-6/1013.25 < 5e-9
print("PASS" if ok else "FAIL")
