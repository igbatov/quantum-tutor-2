# Claim: objective collapse "localizes itself at random, so rarely for one electron that a single atom is practically unaffected"
# GRW standard collapse rate lambda = 1e-16 s^-1 per particle (CSL: ~1e-16 to 1e-8 proposed)
yr = 3.156e7
for lam in (1e-16, 1e-8):
    print(f"lambda={lam:g}/s: mean time between collapses {1/lam/yr:.2e} years; prob in 1 s {lam:.0e}; in a 1.6 ns excited-state lifetime {lam*1.6e-9:.1e}")
ok = 1/1e-16/yr > 1e8
print("PASS" if ok else "FAIL")
