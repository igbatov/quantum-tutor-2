# Claims: "drops ... about every 4.9 volts", "254 nm photon carries 4.9 eV", "neighbours at 4.7 and 5.5 eV",
# "an electron that merely bounces off an atom loses only a minute recoil share", photon emission "bar a minute recoil".
from scipy import constants as k
cm = k.h * k.c * 100 / k.e  # eV per cm^-1
lv = {'6s6p 3P0': 37645.080, '6s6p 3P1': 39412.300, '6s6p 3P2': 44042.977}  # NIST ASD, Hg I
ev = {s: v * cm for s, v in lv.items()}
for s, v in ev.items(): print(f"{s}: {v:.3f} eV")
E254 = k.h * k.c / 253.65e-9 / k.e; print(f"photon at 253.65 nm (air): {E254:.3f} eV")
ok = abs(ev['6s6p 3P1'] - 4.9) < 0.05 and abs(E254 - 4.9) < 0.05
ok &= round(ev['6s6p 3P0'], 1) == 4.7 and round(ev['6s6p 3P2'], 1) == 5.5
M = 200.59 * k.atomic_mass; m = k.m_e
frac = 4 * m * M / (m + M)**2; print(f"max elastic energy-loss fraction e- on Hg: {frac:.2e} (at 4.9 eV: {frac*4.9*1e3:.3f} meV)")
ok &= frac < 1e-4
Mh = k.m_p + k.m_e; Eg = 1.889 * k.e
rec = Eg / (2 * Mh * k.c**2); print(f"H-alpha emission recoil fraction: {rec:.2e}")
ok &= rec < 1e-8
print("PASS" if ok else "FAIL")
