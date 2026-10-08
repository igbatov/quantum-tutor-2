# Claim (objective collapse): "persist until the plate, where the vast number of particles involved
# triggers a genuine, random localization within a tiny fraction of a second"
# GRW/CSL standard parameters: lambda = 1e-16 s^-1 per nucleon, r_C = 1e-7 m. Rate for N nucleons whose
# position differs between branches by > r_C: ~ lambda*N (GRW, spread out) up to lambda*N^2 (CSL, clumped within r_C).
import numpy as np
lam=1e-16
A_Ag=108
t_atom_grw=1/(lam*A_Ag); t_atom_csl=1/(lam*A_Ag**2)
yr=3.156e7
print(f"single Ag atom landed at upper vs lower spot: collapse time ~ {t_atom_csl/yr:.1e} yr (CSL) to {t_atom_grw/yr:.1e} yr (GRW)")
# landing heats a few hundred glass atoms locally; they vibrate ~1e-11 m << r_C, so they add essentially nothing
print("glass atoms disturbed by the landing move ~1e-11 m << r_C = 1e-7 m: no extra collapse rate")
for N in [1e15,1e18,1e20,1e23]:
    print(f"macroscopic record with N={N:.0e} nucleons displaced > r_C: t ~ 1/(lambda N) = {1/(lam*N):.0e} s")
ok_plate_alone = t_atom_csl < 1.0
print("Fast localization happens only once the dot is amplified into a large-scale record (developed deposit,"
      " detector current), not when one atom lands on the glass plate.")
print("PASS" if ok_plate_alone else "FAIL")
