# Claims: "An electron's wavelength is a tiny length that shrinks as its momentum ... grows";
# everyday objects: "wavelengths far smaller than an atomic nucleus"; C60 stripes seen.
from scipy.constants import h, m_e, e, c, atomic_mass
import numpy as np
def lam_e(KeV):  # relativistic electron wavelength for kinetic energy in eV
    K = KeV*e
    p = np.sqrt(K**2 + 2*K*m_e*c**2)/c
    return h/p
for K in [10, 100, 1e3, 50e3]:
    print(f"electron K={K:g} eV: lambda = {lam_e(K):.3e} m")
lams = [lam_e(K) for K in [10, 100, 1e3, 50e3]]
mono = all(np.diff(lams) < 0)
nucleus = 1e-14  # generous upper size of a nucleus (~1-15 fm)
objs = {"1 g bead at 1 m/s": (1e-3, 1.0), "baseball 0.145 kg at 40 m/s": (0.145, 40.0),
        "walking person 70 kg at 1.4 m/s": (70, 1.4), "dust grain 1 microgram at 1 mm/s": (1e-9, 1e-3)}
small = True
for k, (m, v) in objs.items():
    lam = h/(m*v); print(f"{k}: lambda = {lam:.2e} m, ratio to 1e-14 m nucleus = {lam/nucleus:.1e}")
    small &= lam < 1e-3*nucleus
m60 = 60*12*atomic_mass
print(f"C60 at 200 m/s: lambda = {h/(m60*200):.2e} m (Arndt et al. 1999 used ~220 m/s, lambda ~2.5 pm)")
print("PASS" if (mono and small and lams[0] < 1e-9) else "FAIL")
