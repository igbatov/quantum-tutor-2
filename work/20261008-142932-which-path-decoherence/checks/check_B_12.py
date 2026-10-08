# Claims: de Broglie at 100 m/s: electron ~7 um, C70 ~1.4e-24 kg ~5 pm, dust 1e-12 kg ~7e-24 m;
# 10 um grain ~1e-12 kg; grain 1e-12 kg at 1 mm/s: "under a billionth of a nanometre, a thousand times
# smaller than an atomic nucleus".
import numpy as np
from scipy import constants as C
h = C.h
mC70 = 70*12.011*C.atomic_mass
for name, m, tgt in [("electron", C.m_e, 7e-6), ("C70", mC70, 5e-12), ("dust", 1e-12, 7e-24)]:
    lam = h/(m*100); print(f"{name}: m={m:.3e} kg, lambda={lam:.3e} m (text ~{tgt:.0e})")
for rho in [1000, 2000, 3000]:
    print(f"10 um diameter sphere, rho={rho}: m = {rho*np.pi/6*(10e-6)**3:.2e} kg")
lam = h/(1e-12*1e-3)
print(f"grain at 1 mm/s: lambda = {lam:.2e} m; < 1e-18 m: {lam < 1e-18}; nucleus(1e-15 m)/lambda = {1e-15/lam:.0f}, proton radius 0.84e-15/lambda = {0.84e-15/lam:.0f}")
ok = abs(np.log10(h/(C.m_e*100)/7e-6))<0.1 and abs(mC70/1.4e-24-1)<0.02 and abs(np.log10(h/(mC70*100)/5e-12))<0.1 and lam<1e-18 and 500<1e-15/lam<5000
print("PASS" if ok else "FAIL")
