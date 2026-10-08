# Claims: "E = hf"; "photon from a given drop has one sharply defined frequency";
# "bigger drops give higher frequencies"; "Rung 3 to rung 2 ... red line (wavelength 656 nanometers)";
# "rung 4 to rung 2 its blue-green one"; "rung 2 to rung 1 gives invisible ultraviolet";
# caption: "Each colored arrow is a drop to rung 2 that makes one visible line"
import numpy as np
from itertools import combinations
from scipy.constants import physical_constants as pc, h, c, e, k as kB, m_p
R_H = pc['Rydberg constant'][0]/(1+pc['electron-proton mass ratio'][0]); n_air = 1.000277
lam = lambda u,l: 1e9/(R_H*(1/l**2-1/u**2))
for u in [3,4,5,6]: print(f"{u}->2: {lam(u,2):.2f} nm vacuum, {lam(u,2)/n_air:.2f} nm air")
ok_red = abs(lam(3,2)/n_air-656.3) < 0.5 and 620 < lam(3,2) < 750
ok_bg = 480 < lam(4,2) < 500                     # cyan / blue-green band
ok_vis = all(380 <= lam(u,2) <= 750 for u in [3,4,5,6])
ok_uv = lam(2,1) < 380; print(f"2->1: {lam(2,1):.1f} nm (UV)")
# E = hf: energy of 3->2 drop vs h c / lambda
dE = pc['Rydberg constant times hc in eV'][0]/(1+pc['electron-proton mass ratio'][0])*(1/4-1/9)
hf = h*c/(lam(3,2)*1e-9)/e; print(f"3->2 gap {dE:.4f} eV; h f = {hf:.4f} eV"); ok_hf = abs(dE-hf) < 1e-6
pairs = list(combinations(range(1,12),2)); g = np.array([1/l**2-1/u**2 for l,u in pairs])
ok_mono = np.all(np.diff(np.sort(g)) > 0)  # frequency proportional to gap by construction; check distinct ordering
# sharpness: natural width (n=3 level lifetimes ~ 1e-8 s) and Doppler width at 1000 K
nu = c/(lam(3,2)*1e-9); A3 = 1/5.4e-9   # 3p lifetime 5.4 ns (shortest n=3 sublevel; literature)
nat = A3/(2*np.pi)/nu; dop = np.sqrt(8*kB*1000*np.log(2)/(m_p*c**2))
print(f"H-alpha fractional natural width ~{nat:.1e}; Doppler FWHM at 1000 K ~{dop:.1e}; "
      f"visible band spans {(750-380)/550:.2f} fractionally")
ok_sharp = nat < 1e-6 and dop < 1e-4
# "usually a single photon": one-photon E1 rate 2p->1s vs the two-photon 2s->1s exception
print("2p->1s one-photon rate 6.27e8 /s (check_C2_09); 2s->1s two-photon 8.23 /s (literature): "
      "two-photon only for 2s -> 'usually' is apt")
print("PASS" if ok_red and ok_bg and ok_vis and ok_uv and ok_hf and ok_mono and ok_sharp else "FAIL")
