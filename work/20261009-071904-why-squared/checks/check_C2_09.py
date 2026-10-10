# "objective collapse only up to departures far too small to see in these experiments"
# Order of magnitude with GRW's rate lambda = 1e-16 s^-1 per nucleon (GRW 1986) and, generously, the much larger
# CSL value proposed by Adler (1e-8 s^-1). Assumed: molecule of ~1000 u (Cotter et al. 2017 used molecules of
# several hundred u), flight time ~10 ms. Photons carry no nucleons, so GRW localization does not act on them.
# Compare with the experimental precision of about 1e-2.
lam_grw, lam_adler = 1e-16, 1e-8
N_nucleons, t = 1000, 1e-2
p_grw, p_adler = lam_grw*N_nucleons*t, lam_adler*N_nucleons*t
print(f"collapse probability per molecule during flight: GRW {p_grw:.0e}, Adler-CSL {p_adler:.0e}; precision ~1e-2")
print("PASS" if max(p_grw, p_adler) < 1e-4 else "FAIL")
