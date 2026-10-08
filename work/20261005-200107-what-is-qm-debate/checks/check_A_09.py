# Claim: "A drop to a lower energy releases ... one photon, whose energy sets its colour: one sharp colour per kind of drop"
# Check: hydrogen Balmer lines E_n=-13.6/n^2 eV -> discrete visible wavelengths (656, 486, 434, 410 nm)
from scipy.constants import h, c, e, physical_constants
Ry = physical_constants['Rydberg constant times hc in eV'][0]
mu_corr = 1/(1 + physical_constants['electron-proton mass ratio'][0])
lines = []
for n in [3,4,5,6]:
    dE = Ry*mu_corr*(1/4 - 1/n**2)
    lam_vac = h*c/(dE*e)*1e9
    lines.append(lam_vac); print(f"n={n}->2: dE={dE:.4f} eV, lambda(vac)={lam_vac:.2f} nm")
ref = [656.47, 486.27, 434.17, 410.29]  # vacuum wavelengths (NIST)
ok = all(abs(a-b) < 0.2 for a, b in zip(lines, ref))
print("PASS" if ok else "FAIL")
