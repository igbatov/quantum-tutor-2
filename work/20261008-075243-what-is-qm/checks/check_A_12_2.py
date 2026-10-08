# Claims: "Each electron makes one whole dot, at a spot nobody can predict"; "After thousands of electrons
# the dots form bright and dark stripes"; figure note: "a few dots land even far from the centre".
import numpy as np
rng = np.random.default_rng(2026)
X = np.linspace(-8, 8, 160001); P = np.cos(np.pi*X)**2*np.sinc(X/4)**2
cdf = np.cumsum(P); cdf /= cdf[-1]
samp = np.interp(rng.random(10000), cdf, X)
far = np.mean(abs(samp) > 4)
exact_far = 1 - (np.interp(4, X, cdf) - np.interp(-4, X, cdf))
print(f"fraction beyond |X|>4: sampled {far:.3f}, exact {exact_far:.3f}")
def contrast(s):
    near_bright = np.sum(abs(s - np.round(s)) < 0.15)       # within 0.15 of integer X
    near_dark = np.sum(abs(s - np.round(s-0.5) - 0.5) < 0.15)
    return near_bright, near_dark
for N in (10, 100, 1000, 10000):
    b, dk = contrast(samp[:N]); print(f"N={N:5d}: dots near bright lines {b}, near dark lines {dk}")
b, dk = contrast(samp[:1000])
ok = 0.01 < exact_far < 0.15 and b > 10*max(dk, 1)
print("PASS" if ok else "FAIL")
