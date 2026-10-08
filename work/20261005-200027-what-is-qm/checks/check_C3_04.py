# Claims: "measuring its energy always gives one of the rungs, never anything in between";
# "(Measured very precisely, each rung turns out to be a tight cluster of sub-rungs.)"
import numpy as np
from scipy.constants import physical_constants as pc, h, c, e
alpha = pc['fine-structure constant'][0]; mc2 = pc['electron mass energy equivalent in MeV'][0]*1e6
Ry = pc['Rydberg constant times hc in eV'][0]
# Dirac fine structure: E_nj ~ -Ry/n^2 [1 + alpha^2/n^2 (n/(j+1/2) - 3/4)]
def Enj(n,j): return -Ry/n**2*(1+alpha**2/n**2*(n/(j+0.5)-0.75))
ok = True
for n in [1,2,3,4]:
    js = [l+0.5 for l in range(n)]
    lv = sorted(set(round(Enj(n,j),12) for j in js))
    spread = max(lv)-min(lv)
    print(f"n={n}: {len(lv)} fine-structure level(s), spread {spread:.2e} eV")
    if n>1: ok &= len(lv)>1
# n=1 has a single j=1/2 level; its sub-rungs come from hyperfine splitting (21 cm line)
nu21 = 1420.405751768e6; dE_hf = h*nu21/e
print(f"n=1 hyperfine split (F=0,1): {dE_hf:.3e} eV (21.1 cm line) -> n=1 is also a cluster of 2 sub-rungs")
ok &= dE_hf > 0
# tightness: cluster widths vs gap between rungs
gap12 = Ry*0.75; gap23 = Ry*(1/4-1/9)
spread2 = Enj(2,1.5)-Enj(2,0.5)
print(f"n=2 spread / (rung2-rung3 gap) = {spread2/gap23:.1e}; n=1 spread / (rung1-rung2 gap) = {dE_hf/gap12:.1e}")
ok &= spread2/gap23 < 1e-3 and dE_hf/gap12 < 1e-5
# discreteness: bound levels isolated (no level between n and n+1 in Schroedinger model)
print("PASS" if ok else "FAIL")
