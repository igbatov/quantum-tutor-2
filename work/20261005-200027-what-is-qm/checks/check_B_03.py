# Claim: "A mere sieve, sorting photons by some fixed property, could never do that."
# Model: each photon has a fixed hidden property lam; each filter passes it with prob p_f(lam)
# and leaves lam unchanged. Then P(pass V,45,H) = E[pV p45 pH] <= E[pV pH] = P(pass V,H).
import numpy as np
rng = np.random.default_rng(0)
worst = -np.inf
for _ in range(20000):
    K = rng.integers(1, 20)
    w = rng.dirichlet(np.ones(K))           # distribution of hidden property values
    pV, p45, pH = rng.random((3, K))        # arbitrary pass probabilities per value
    three = np.sum(w*pV*p45*pH); two = np.sum(w*pV*pH)
    worst = max(worst, three - two)
print("max over 20000 random sieve models of [3-filter - 2-filter] =", worst)
print("quantum: 3-filter 0.25 vs 2-filter 0.0 per photon after V")
print("PASS" if worst <= 1e-15 else "FAIL")
