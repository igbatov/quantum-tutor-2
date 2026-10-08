# Claim: amplitudes "like little arrows ... cancel when they point opposite ways"
import numpy as np
th = np.linspace(0, 2*np.pi, 721)
P = np.abs(1 + np.exp(1j*th))**2          # two unit arrows, relative angle th
zero_at = th[np.isclose(P, 0, atol=1e-12)]
print("|1+e^{i th}|^2 = 0 only at th =", zero_at, "(pi =", np.pi, ")")
print("range of P:", P.min().round(12), "to", P.max())
ok = len(zero_at) == 1 and np.isclose(zero_at[0], np.pi) and np.isclose(P.max(), 4)
print("PASS" if ok else "FAIL")
