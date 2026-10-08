# Claims: "rung 3 to rung 2 gives hydrogen's red line (656 nm)", "rung 4 to rung 2 its blue-green one",
# "bigger drops make bluer light", "E = hf", and "So each gap makes one sharp color" (+ "which your eye sees as color").
import numpy as np
from itertools import combinations
from scipy.constants import physical_constants as pc, h, c, e
R_H = pc['Rydberg constant'][0]/(1+pc['electron-proton mass ratio'][0]); n_air = 1.000277
lam = lambda u,l: 1e9/(R_H*(1/l**2-1/u**2))   # vacuum nm
claimed = {3:656.3,4:486.1,5:434.0,6:410.2}
ok_bal = all(abs(lam(u,2)/n_air-v)<0.3 for u,v in claimed.items())
for u in claimed: print(f"{u}->2: {lam(u,2)/n_air:.2f} nm (air)")
ok_colors = 620<lam(3,2)<750 and 480<lam(4,2)<500
# E = hf dimension and value
dE = 13.6057*(1/4-1/9); print(f"3->2 photon {dE:.3f} eV; hc/656.47nm = {h*c/(lam(3,2)*1e-9)/e:.3f} eV")
# bigger drop -> shorter wavelength, over all pairs among n<=8
pairs = list(combinations(range(1,9),2))
gaps = np.array([R_H*(1/l**2-1/u**2) for l,u in pairs]); lams = 1e9/gaps
ok_mono = np.all(np.diff(lams[np.argsort(gaps)])<0)
# how many gaps among n<=8 give visible light (380-750 nm)?
vis = [(u,l,round(1e9/g,1)) for (l,u),g in zip(pairs,gaps) if 380<1e9/g<750]
print(f"pairs among rungs 1-8: {len(pairs)}; visible: {len(vis)} -> {vis}")
print(f"examples invisible: 2->1 {lam(2,1):.1f} nm (UV), 4->3 {lam(4,3):.0f} nm (IR)")
ok_each_color = len(vis)==len(pairs)
print("656 nm / blue-green / E=hf:", "PASS" if ok_bal and ok_colors else "FAIL")
print("bigger drops bluer:", "PASS" if ok_mono else "FAIL")
print("'each gap makes one sharp color':", "PASS" if ok_each_color else
      "FAIL (each gap makes one sharp frequency; most gaps are UV or IR, not a color)")
print("PASS" if ok_bal and ok_colors and ok_mono and ok_each_color else "FAIL")
# Note (real setup): fine structure splits rung 2 into j=1/2 and j=3/2 (Dirac): dE = alpha^4 m c^2 (1/1 - 1/2)/(2 n^3)... 
alpha = pc['fine-structure constant'][0]; mc2 = pc['electron mass energy equivalent in MeV'][0]*1e6
dE2 = alpha**4*mc2/(2*2**3)*(1/1-1/2)   # n=2: E_nj ~ -(alpha^4 mc^2/2n^3)(n/(j+1/2) - 3/4)
dlam = (656.47e-9)**2*dE2*e/(h*c)*1e9
print(f"note: n=2 fine-structure split {dE2:.2e} eV -> H-alpha components ~{dlam:.3f} nm apart (same color to the eye)")
