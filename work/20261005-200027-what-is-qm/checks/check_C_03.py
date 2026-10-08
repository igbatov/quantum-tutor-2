# Claims: "rung 3 to rung 2 gives hydrogen's red line (wavelength 656 nanometers)",
# "rung 4 to rung 2 its blue-green one"; figure: 486, 434, 410 nm; 2->1 "ultraviolet (invisible)";
# "bigger drops make bluer light"; E = hf
import numpy as np
from scipy.constants import physical_constants as pc, h, c, e
R_inf = pc['Rydberg constant'][0]
R_H = R_inf/(1+pc['electron-proton mass ratio'][0])
n_air = 1.000277  # approx refractive index of air in the visible
lines = {}
for n in [3,4,5,6]:
    lam_vac = 1/(R_H*(1/4-1/n**2))
    lines[n] = lam_vac
    dE = h*c/lam_vac/e
    print(f"{n}->2: vac {lam_vac*1e9:.2f} nm, air {lam_vac/n_air*1e9:.2f} nm, photon {dE:.3f} eV")
claimed = {3:656.3,4:486.1,5:434.0,6:410.2}
ok = all(abs(lines[n]/n_air*1e9-claimed[n])<0.3 for n in claimed)
lam21 = 1/(R_H*(1-1/4))*1e9
print(f"2->1: {lam21:.1f} nm (UV if < 380)")
# 13.6(1/4-1/9) vs hc/656nm
print("E=hf check:", 13.6057*(1/4-1/9), h*c/656.3e-9/e)
mono = all(lines[n] > lines[n+1] for n in [3,4,5])  # bigger drop -> shorter wavelength
colors_ok = 620<lines[3]*1e9<750 and 480<lines[4]*1e9<500
print("PASS" if ok and lam21<380 and mono and colors_ok else "FAIL")
