# Claim: "four bright visible lines are red, blue-green, blue and violet (656, 486, 434 and 410 nanometres)"
# Claim: "122 nm: ultraviolet, invisible" (rung 2 -> rung 1)
# Claim: "bigger drops give higher frequencies, towards blue and violet"
import numpy as np
from scipy import constants as C
R_inf = C.Rydberg
mu_ratio = C.m_p/(C.m_e+C.m_p)
R_H = R_inf*mu_ratio
def lam_vac(n_up, n_low): return 1/(R_H*(1/n_low**2-1/n_up**2))*1e9
# refractive index of air ~1.000277 for visible (standard air)
n_air = 1.000277
claimed = {3:656, 4:486, 5:434, 6:410}
ok = True
gaps = []
for nu, c in claimed.items():
    lv = lam_vac(nu, 2); la = lv/n_air
    gaps.append(13.6057*(1/4-1/nu**2))
    good = abs(la-c) < 1.0
    ok &= good
    print(f"{nu}->2: vacuum {lv:.2f} nm, air {la:.2f} nm, claimed {c}  {'ok' if good else 'MISMATCH'}")
# colour bands (approx): red 620-750, cyan/blue-green 485-500, blue 430-485 / violet 380-450
print("486 nm sits at blue/cyan boundary (blue-green: reasonable); 434 nm blue-violet; 410 violet")
lya = lam_vac(2,1)
print(f"2->1: {lya:.2f} nm (claimed 122, UV if < 380): {'ok' if abs(lya-122)<1 and lya<380 else 'MISMATCH'}")
ok &= abs(lya-122) < 1 and lya < 380
# bigger drop => shorter wavelength
lams = [lam_vac(n,2) for n in (3,4,5,6)]
mono = np.all(np.diff(gaps) > 0) and np.all(np.diff(lams) < 0)
print(f"energy gaps (eV) {np.round(gaps,3)}, wavelengths decrease as gap grows: {mono}")
ok &= mono
# All Lyman (->1) lines in UV:
lyman_max = lam_vac(2,1)
print(f"longest Lyman line {lyman_max:.1f} nm < 380 nm: {lyman_max<380}")
ok &= lyman_max < 380
print("PASS" if ok else "FAIL")
