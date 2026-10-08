# Claims (objective collapse): "faint warming and faint radiation from ordinary matter";
# "for one electron the difference is far too small to see, it grows with the amount of matter"
import numpy as np
from scipy.constants import hbar, m_p, m_e, N_A, e, c
lam, rC = 1e-16, 1e-7          # GRW/CSL standard values (s^-1, m)
# heating: each localization gives momentum kicks; dE/dt = lam hbar^2/(4 m rC^2) per particle (GRW)
P_nuc = lam*hbar**2/(4*m_p*rC**2)
print(f"GRW heating per nucleon {P_nuc:.1e} W; per kg of matter {P_nuc/m_p:.1e} W; dT/dt for water ~{P_nuc/m_p/4184*3.15e7:.1e} K/yr")
# visibility loss in interferometry: decay rate ~ lam * N^2 (CSL, object < rC, mass-proportional) or ~lam*N (GRW, >rC)
t = 1e-3   # time in interferometer
for name, N in [("electron", m_e/m_p), ("C60", 720), ("25 kDa molecule", 2.5e4), ("1 um grain", 3e11)]:
    G_N2 = lam*N**2      # CSL coherent amplification for objects smaller than rC
    G_N = lam*N
    print(f"{name:16s} N={N:.1e}: fringe loss over 1 ms, CSL(N^2) {1-np.exp(-G_N2*t):.1e}, GRW(N) {1-np.exp(-G_N*t):.1e}")
ok = P_nuc > 0 and P_nuc/m_p < 1e-10 and lam*(m_e/m_p)**2*t < 1e-20 and lam*(3e11)**2*t > 1
print("PASS (warming exists but is tiny; effect negligible for one electron and grows with mass)" if ok else "FAIL")
