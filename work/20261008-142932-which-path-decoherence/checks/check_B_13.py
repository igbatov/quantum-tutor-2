# Claim: 1998 microwave photon kick "about a hundred thousand times smaller than the kick of the laser
# light used to split the atoms' paths" (Durr, Nonn & Rempe: 85Rb hyperfine 3.04 GHz; Bragg at 780 nm, 2hbar k).
import numpy as np
from scipy import constants as C
lam_L = 780.24e-9
for iso, f in [("85Rb", 3.0357e9), ("87Rb", 6.8347e9)]:
    lam_mw = C.c/f
    print(f"{iso}: microwave lambda={lam_mw*100:.1f} cm; one-photon ratio {lam_mw/lam_L:.2e}; vs Bragg 2hbar k: {2*lam_mw/lam_L:.2e}")
r = 2*(C.c/3.0357e9)/lam_L
print("PASS" if 3e4 < r < 3e5 else "FAIL")
