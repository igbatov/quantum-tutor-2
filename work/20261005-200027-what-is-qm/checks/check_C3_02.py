# Claims: "every atom of ordinary hydrogen has the same allowed energies";
# "hydrogen's energies crowd together toward the top, while an ideal string's frequencies are evenly spaced";
# figure: ladder to scale, grey higher rungs crowd toward the "set free" line (E=0)
import numpy as np
from scipy.constants import physical_constants as pc, m_e
Ryinf = pc['Rydberg constant times hc in eV'][0]
mH = pc['proton mass'][0]; mD = pc['deuteron mass'][0]
EH = lambda n: -Ryinf/(1+m_e/mH)/n**2; ED = lambda n: -Ryinf/(1+m_e/mD)/n**2
# ordinary hydrogen: ladder fixed by constants alone (no free parameter) -> same for every 1H atom
print("1H levels n=1..6 (eV):", [round(EH(n),3) for n in range(1,7)])
# why "ordinary" is needed: deuterium differs
R = pc['Rydberg constant'][0]
lamH = 1e9/(R/(1+m_e/mH)*(1/4-1/9)); lamD = 1e9/(R/(1+m_e/mD)*(1/4-1/9))
print(f"H-alpha: 1H {lamH:.3f} nm vs 2H {lamD:.3f} nm (vacuum) -> qualifier 'ordinary' is needed and present")
ok_ord = abs(lamH-lamD) > 0.1
gaps = np.diff([EH(n) for n in range(1,40)]); ok_crowd = np.all(np.diff(gaps) < 0) and EH(39) > -0.01
print("H gaps n=1..6:", np.round(gaps[:5],3), "; E_39 =", round(EH(39),4), "eV (-> 0)")
n = np.arange(1,20); ok_string = np.allclose(np.diff(n*1.0), 1.0)   # ideal string f_n = n f1
print("ideal string f_n = n f1 evenly spaced:", ok_string)
print("PASS" if ok_ord and ok_crowd and ok_string else "FAIL")
