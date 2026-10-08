# Claim: "each ball uses one slit, so a second slit could only add hits, and (3) shows it took hits away"
import numpy as np
rng = np.random.default_rng(0)
# any classical ensemble: P_both = P_L + P_R with P_L, P_R >= 0  => P_both >= P_L pointwise
PL = rng.random((1000, 50)); PR = rng.random((1000, 50))
classical_ok = np.all(PL + PR >= PL)
X = np.linspace(-3, 3, 6001); P1 = np.sinc(X/4)**2; Pb = 4*P1*np.cos(np.pi*X)**2
quantum_takes = np.any(Pb < P1 - 1e-6)
print("classical: P_both >= P_one everywhere:", classical_ok, "| quantum model has P_both < P_one somewhere:", quantum_takes)
print("PASS" if classical_ok and quantum_takes else "FAIL")
