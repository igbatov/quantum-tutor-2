# Claim: a classical wave split between two exits makes click-producing detectors "click together at least as often
# as independent random clicks at the same rates" (anticorrelation parameter alpha >= 1); also "Tiny balls":
# two-slit count = sum of single-slit counts, so opening a slit never lowers a count.
# Model: pulse intensity I (any random distribution), exits get T*I and R*I; click prob in a gate ~ eta*intensity (weak).
import numpy as np
rng=np.random.default_rng(5); ok=True; amin=np.inf
for _ in range(2000):
    I=rng.gamma(rng.uniform(0.2,5),size=4000)*rng.uniform(0.1,3); T=rng.uniform(0.05,0.95); R=1-T; eta=1e-3
    pt,pr=eta*T*I,eta*R*I                          # per-gate click probabilities (Poisson, weak)
    pc=np.mean((1-np.exp(-pt))*(1-np.exp(-pr)))   # coincidences
    alpha=pc/(np.mean(1-np.exp(-pt))*np.mean(1-np.exp(-pr))); amin=min(amin,alpha)
print("min alpha over random classical pulse statistics:",amin," (Grangier et al. single photons: ~0.18, literature)")
ok&=amin>=1-1e-9
nA,nB=rng.uniform(0,1,1000),rng.uniform(0,1,1000); ok&=np.all(nA+nB>=np.maximum(nA,nB))
print("PASS" if ok else "FAIL")
