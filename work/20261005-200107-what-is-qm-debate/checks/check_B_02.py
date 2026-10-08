# Claim: "E_n = -13.6/n^2 eV ... (-13.6, -3.40, -1.51, -0.85, -0.54, -0.38 eV)"
# and hydrogen has a lowest rung at -13.6 eV derived from constants.
import numpy as np
from scipy import constants as C
mu = C.m_e*C.m_p/(C.m_e+C.m_p)
E1 = mu*C.e**4/(2*(4*np.pi*C.epsilon_0)**2*C.hbar**2)/C.e  # eV, reduced mass
print(f"|E1| (reduced mass) = {E1:.4f} eV")
claimed = [-13.6, -3.40, -1.51, -0.85, -0.54, -0.38]
ok = abs(E1-13.6) < 0.01
for n, c in zip(range(1,7), claimed):
    v = -E1/n**2
    good = abs(v-c) < 0.006 + 0.005*abs(c)
    ok &= good
    print(f"n={n}: computed {v:.3f} eV, claimed {c}  {'ok' if good else 'MISMATCH'}")
print("PASS" if ok else "FAIL")
