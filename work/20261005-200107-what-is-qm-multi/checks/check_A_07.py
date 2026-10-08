# Claim: "how likely an excited atom is to give off its photon within the next nanosecond"
# Plausibility: H 2p lifetime from A = (2^8/3^8) * alpha^5 * m c^2/hbar ... use known formula A_2p->1s
from scipy.constants import alpha, m_e, c, hbar
import math
A = (2/3)**8 * alpha**5 * m_e*c**2/hbar   # A(2p->1s) = (2/3)^8 alpha^5 m c^2 / hbar
tau = 1/A
print(f"A = {A:.3e} /s, tau(2p) = {tau*1e9:.2f} ns")
P1ns = 1-math.exp(-1e-9/tau)
print(f"P(decay within 1 ns) = {P1ns:.2f}")
print("PASS" if 0.1e-9 < tau < 100e-9 else "FAIL")
