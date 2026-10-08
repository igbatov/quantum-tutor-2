# Claim: "Hydrogen's visible lines are red, blue-green, blue-violet and violet" (656, 486, 434, 410 nm from n=3..6 -> 2)
# Also: "a bigger drop gives bluer light"; "drops to level 1 give ultraviolet light"
import numpy as np
from scipy.constants import physical_constants, h, c, e
Rinf = physical_constants['Rydberg constant'][0]
me = physical_constants['electron mass'][0]; mp = physical_constants['proton mass'][0]
RH = Rinf/(1+me/mp)
def lam_air(nu, nl):
    lv = 1/(RH*(1/nl**2 - 1/nu**2))  # vacuum
    # Edlen-type air refractive index ~1.000277
    return lv/1.000277, lv
balmer = {nu: lam_air(nu, 2) for nu in (3, 4, 5, 6)}
claimed = {3: 656, 4: 486, 5: 434, 6: 410}
ok = True
for nu, (la, lv) in balmer.items():
    print(f"n={nu}->2: air {la*1e9:.2f} nm, vacuum {lv*1e9:.2f} nm, claimed {claimed[nu]}")
    ok &= abs(la*1e9 - claimed[nu]) < 1.0
# colour bands (approx): violet 380-450, blue 450-495, cyan/blue-green 485-500, red 620-750
cols = {3: 620 <= balmer[3][0]*1e9 <= 750, 4: 480 <= balmer[4][0]*1e9 <= 500,
        5: 425 <= balmer[5][0]*1e9 <= 450, 6: 380 <= balmer[6][0]*1e9 <= 425}
print("colour bands consistent:", cols)
ok &= all(cols.values())
# bigger drop -> shorter wavelength
lams = [balmer[n][0] for n in (3, 4, 5, 6)]
ok &= all(np.diff(lams) < 0)
# n>=7 -> 2 are below 400 nm? (only 4 'visible' lines claimed)
l7 = lam_air(7, 2)[0]*1e9
print(f"n=7->2: {l7:.1f} nm (near-UV edge of visibility)")
# Lyman series: all < 380 nm
ly = [lam_air(nu, 1)[1]*1e9 for nu in range(2, 50)]
print(f"Lyman range: {min(ly):.1f}-{max(ly):.1f} nm")
ok &= max(ly) < 380
print("PASS" if ok else "FAIL")
