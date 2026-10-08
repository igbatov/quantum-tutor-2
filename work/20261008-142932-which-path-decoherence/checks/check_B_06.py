# Claims: C70 "about 840 times the mass of a hydrogen atom"; room-temperature gas atom wavelength
# "a few hundredths of a nanometre", "tens of thousands of times shorter than the micrometre";
# Talbot-Lau grating spacing "a few tens of centimetres"; air "wavelength a few hundredths of a nm".
import numpy as np
from scipy import constants as C
u = C.atomic_mass; h = C.h; kB = C.k
mC70 = 70*12.011; mH = 1.00794
print(f"C70/H mass ratio = {mC70/mH:.0f} (C70 = {mC70:.1f} u)")
T = 295
for name, m in [("argon", 39.948), ("N2", 28.014), ("air avg", 28.97)]:
    v = np.sqrt(3*kB*T/(m*u)); lam = h/(m*u*v)
    print(f"{name}: v_rms={v:.0f} m/s, lambda={lam*1e9:.4f} nm, 1 um/lambda = {1e-6/lam:.0f}")
# Talbot length L = d^2/lambda_dB for C70, d = 991 nm, v = 100-200 m/s
for v in [100, 150, 200]:
    lam = h/(mC70*u*v); print(f"C70 v={v} m/s: lambda={lam*1e12:.2f} pm, Talbot L={991e-9**2/lam*100:.0f} cm")
lamAr = h/(39.948*u*np.sqrt(3*kB*T/(39.948*u)))
ok = abs(mC70/mH-840) < 10 and 0.01e-9 < lamAr < 0.05e-9 and 1e4 < 1e-6/lamAr < 1e5
print("PASS" if ok else "FAIL")
