# Claim: "a 254 nm photon carries 4.9 eV"; "mercury has a rung 4.9 eV above its lowest"
from scipy import constants as k
hc_eVnm = k.h*k.c/k.e*1e9
E254 = hc_eVnm/253.7
# NIST Hg I level 6s6p 3P1 = 39412.300 cm^-1
E3P1 = 39412.300*100*k.h*k.c/k.e
lam3P1 = 1e7/39412.300
print(f"E(253.7 nm)={E254:.3f} eV; Hg 6s6p 3P1 level={E3P1:.3f} eV; its decay wavelength (vac) {lam3P1:.2f} nm")
ok = abs(E254-4.9) < 0.05 and abs(E3P1-4.9) < 0.05
print("PASS" if ok else "FAIL")
