# Check-yourself: "Would a smaller dot glow redder or bluer?" Expected answer: bluer.
# Also: "anything confined ... has a ladder of allowed energies" (particle in a box).
import numpy as np
from scipy import constants as C
m_eff = 0.1*C.m_e   # illustrative effective mass
def gap(L):  # E2 - E1 for infinite well
    return (4-1)*np.pi**2*C.hbar**2/(2*m_eff*L**2)/C.e
for L in [6e-9, 4e-9, 3e-9]:
    g = gap(L); print(f"L={L*1e9:.0f} nm: E2-E1={g:.3f} eV, photon {C.h*C.c/(g*C.e)*1e9:.0f} nm")
ok = gap(3e-9) > gap(6e-9)
print("smaller box -> larger gap -> shorter wavelength (bluer):", ok)
print("PASS" if ok else "FAIL")
