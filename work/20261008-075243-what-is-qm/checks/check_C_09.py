# Claim: "hydrogen's rungs are not evenly spaced but crowd together towards the top, where the electron comes free"
# Claim (fig): E_n = -13.6/n^2: -13.6, -3.40, -1.51, -0.85, -0.54, -0.38 eV; "No rung lies below it"
import numpy as np
from scipy import constants as k
Ry = k.physical_constants['Rydberg constant times hc in eV'][0]/(1+k.m_e/k.m_p)
n = np.arange(1, 50); E = -Ry/n**2
print("E_1..6 =", np.round(E[:6], 2), "Ry_H =", round(Ry, 3))
claimed = np.array([-13.6, -3.40, -1.51, -0.85, -0.54, -0.38])
ok = np.allclose(E[:6], claimed, atol=0.01)
gaps = np.diff(E)
print("gaps:", np.round(gaps[:6], 3), "strictly decreasing:", np.all(np.diff(gaps) < 0))
ok &= np.all(np.diff(gaps) < 0) and np.all(E < 0) and abs(E[-1]) < 0.01 and E.min() == E[0]
print("limit n->inf: E ->", E[-1], "(0 = electron free)")
print("PASS" if ok else "FAIL")
