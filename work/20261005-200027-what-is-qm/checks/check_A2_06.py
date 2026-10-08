# Claim: "well-isolated molecules of hundreds of atoms still make stripes" (empirical)
from scipy import constants as c
for name, amu, v in [("C60 (60 atoms) @ 200 m/s", 720, 200), ("~2000-atom molecule (~25,000 u) @ 250 m/s", 25000, 250)]:
    print(f"{name}: de Broglie wavelength = {c.h/(amu*c.atomic_mass*v):.3e} m")
print("UNVERIFIABLE by computation (empirical; consistent with Arndt et al. 1999, Fein et al. 2019)")
