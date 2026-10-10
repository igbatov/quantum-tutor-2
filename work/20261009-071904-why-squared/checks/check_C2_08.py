# "the two detectors click together far less often than any wave, which would have to split, could manage"
# Classical wave split by a half-silvered mirror: transmitted T*I, reflected R*I, click rates proportional to
# intensity. Coincidence ratio alpha = <I_t I_r>/(<I_t><I_r>) = <I^2>/<I>^2 >= 1 (Cauchy-Schwarz) for ANY
# fluctuating intensity. A single photon goes one way: alpha = 0.
import numpy as np
rng = np.random.default_rng(5)
alphas = []
for dist in [lambda n: np.ones(n), lambda n: rng.exponential(size=n), lambda n: rng.uniform(0, 1, n),
             lambda n: rng.lognormal(0, 1.5, n), lambda n: (rng.random(n) < 0.01)*100.0]:
    I = dist(10**6); T, R = 0.5, 0.5
    alphas.append(np.mean(T*I*R*I)/(np.mean(T*I)*np.mean(R*I)))
print("classical alpha for several intensity statistics:", np.round(alphas, 3), " min", min(alphas))
# single photon: exactly one detector clicks per photon
clicks_t = rng.random(10**6) < 0.5; clicks_r = ~clicks_t
alpha_photon = np.mean(clicks_t & clicks_r)/(np.mean(clicks_t)*np.mean(clicks_r))
print("single-photon alpha:", alpha_photon, "(Grangier-Roger-Aspect 1986 reported about 0.18, literature value, not computed)")
print("PASS" if min(alphas) >= 1-1e-9 and alpha_photon == 0 else "FAIL")
