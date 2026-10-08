# Claim: "A mere sieve ... leaving the ones that pass unchanged, could never do that: an extra sieve can only remove photons"
# Model: each photon carries a fixed hidden property lam; filter at angle a passes it with prob p_a(lam) (0..1),
# survivors unchanged. Then P(V,45,H) = E[p_V p_45 p_H] <= E[p_V p_H] = P(V,H). Test random models.
import numpy as np
rng = np.random.default_rng(2); worst = -np.inf
for trial in range(20000):
    K = rng.integers(1, 30)                        # number of hidden-property values
    w = rng.dirichlet(np.ones(K))
    p = rng.random((3, K)) if trial % 2 else (rng.random((3, K)) < 0.5).astype(float)  # stochastic or deterministic sieves
    with_mid = np.sum(w*p[0]*p[1]*p[2]); without = np.sum(w*p[0]*p[2])
    worst = max(worst, with_mid - without)
print("max over models of P(with 45) - P(without):", worst, " quantum: 0.25 - 0 = 0.25")
print("PASS" if worst <= 1e-15 else "FAIL")
