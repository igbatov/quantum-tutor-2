# Exp 1 geometry: "slits about 200 nanometres apart"; paths "by the middle grating ... a few hundredths of a
# millimetre apart"; "just after the first grating ... less than a couple of micrometres apart" while
# "d from zero to about two photon wavelengths" at 589 nm.
# Assumptions (not in the text, typical of the MIT interferometer): Na at 700-3000 m/s, gratings 0.5-1 m apart.
import numpy as np
from scipy import constants as C
m = 22.98977*C.atomic_mass
for v in [700, 1000, 3000]:
    lam = C.h/(m*v); th = lam/200e-9
    print(f"v={v} m/s: λ_dB={lam*1e12:.1f} pm, first-order angle {th*1e6:.0f} µrad, separation at 0.5 m: {th*0.5*1e6:.0f} µm, at 1 m: {th*1e6:.0f} µm")
print(f"2 photon wavelengths = {2*589e-9*1e6:.2f} µm (< 2 µm: {2*589e-9 < 2e-6})")
v = np.array([700, 1000, 3000]); sep = C.h/(m*v)/200e-9*np.array([0.5, 1.0])[:, None]
print("separations range (µm):", np.round(sep.min()*1e6), "-", np.round(sep.max()*1e6))
print("PASS" if 10e-6 < np.median(sep) < 90e-6 else "FAIL")
