# Captions: b-many-records "with c = 0.02, six events leave under one ten-billionth"; "1/e ≈ 0.37";
# b-dust-grain marks for Δx = 10 µm: "microwave background at Δx/λ ≈ 0.01", "sunlight at ≈ 20", "air ... ≈ 5 × 10⁵".
import numpy as np
from scipy import constants as C
v6 = 0.02**6; print(f"0.02^6 = {v6:.2e} (< 1e-10: {v6 < 1e-10}); 1/e = {np.exp(-1):.3f}")
lam_air = C.h/np.sqrt(3*28.0134*C.atomic_mass*C.k*293.15)   # rms-momentum de Broglie wavelength, N2
lam_air2 = C.h/np.sqrt(2*np.pi*28.0134*C.atomic_mass*C.k*293.15)  # thermal wavelength
print(f"CMB 10 µm/1 mm = {10e-6/1e-3}; sunlight 10 µm/0.5 µm = {10e-6/0.5e-6:.0f}; air: λ = {lam_air*1e9:.3f}-{lam_air2*1e9:.3f} nm -> Δx/λ = {10e-6/lam_air2:.1e}-{10e-6/lam_air:.1e}")
ok = v6 < 1e-10 and 2e5 < 10e-6/lam_air2 and 10e-6/lam_air < 1e6
print("PASS" if ok else "FAIL")
