# Claims (objective collapse): "persist until the atom's arrival is amplified into a large record";
# "For a lone atom the proposed effect is far too weak to show up in any count";
# "The first three views are interpretations: identical counts ... The fourth changes the theory slightly"
import numpy as np
lam=1e-16; A_Ag=108; yr=3.156e7
t_csl=1/(lam*A_Ag**2); t_grw=1/(lam*A_Ag)
print(f"lone Ag atom in two places: collapse time {t_csl/yr:.1e} to {t_grw/yr:.1e} yr")
ok = t_csl > 1e9   # seconds; vastly longer than any flight
# deviation in counts: probability of a collapse during ~1 ms flight / ~10 ms interferometer loop
for t in [1e-3,1e-2]:
    p=lam*A_Ag**2*t
    print(f"probability of a spontaneous collapse during {t:g} s: {p:.1e}  -> change in counts ~{p:.0e}")
    ok &= p<1e-10
for N in [1e18,1e20,1e23]:
    print(f"record with N={N:.0e} nucleons displaced: t ~ {1/(lam*N):.0e} s")
ok &= 1/(lam*1e18) < 1.0
print("changes theory 'slightly': nonzero predicted deviation, but ~1e-14 or less for these counts")
print("PASS" if ok else "FAIL")
