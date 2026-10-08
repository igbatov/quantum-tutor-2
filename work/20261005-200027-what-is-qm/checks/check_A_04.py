# Claim: "well-isolated molecules of hundreds of atoms still make stripes" (empirical; illustrative check)
# Compute de Broglie wavelengths to show they are tiny but nonzero; the claim itself is experimental (Arndt et al.).
from scipy import constants as c
for name, amu, v in [("electron 50 keV", None, None), ("C60 (60 atoms) @ 200 m/s", 720, 200),
                     ("~2000-atom molecule (~25,000 u) @ 250 m/s", 25000, 250)]:
    if amu is None:
        E = 50e3*c.e; p = (E**2 + 2*E*c.m_e*c.c**2)**0.5/c.c
    else:
        p = amu*c.atomic_mass*v
    print(f"{name}: lambda = {c.h/p:.3e} m")
print("UNVERIFIABLE (empirical claim; consistent with published molecule-interference experiments)")
