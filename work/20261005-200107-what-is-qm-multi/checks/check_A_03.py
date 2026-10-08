# Claims: Balmer lines "about 656, 486, 434, 410 nm" from 1/lambda = R_H(1/4 - 1/n^2), R_H=1.0968e7 /m;
# "just four sharp visible colors" ; E_n = -13.6/n^2 eV consistent
import numpy as np
from scipy.constants import physical_constants as pc, h, c, e
RH = 1.0968e7
claimed = {3:656, 4:486, 5:434, 6:410}
ok = True
for n in range(3, 9):
    lam = 1e9/(RH*(0.25-1/n**2))
    # cross-check with energy ladder using reduced-mass Rydberg energy
    Ry_H = pc['Rydberg constant times hc in eV'][0]/(1+pc['electron-proton mass ratio'][0])
    dE = Ry_H*(0.25-1/n**2)
    lamE = h*c/(dE*e)*1e9
    tag = ''
    if n in claimed:
        good = abs(lam-claimed[n]) < 1.0
        ok &= good; tag = f"claimed {claimed[n]} -> {'ok' if good else 'MISMATCH'}"
    print(f"n={n}->2: lambda={lam:.2f} nm (from energies {lamE:.2f} nm) {tag}")
print("Rydberg energy (H, reduced mass) eV:", Ry_H)
# visible lines between 400 and 700 nm
vis = [n for n in range(3,30) if 400 <= 1e9/(RH*(0.25-1/n**2)) <= 700]
print("Balmer lines in 400-700 nm:", vis, "count", len(vis))
ok &= len(vis) == 4
print("PASS" if ok else "FAIL")
