# Caption claim (fig b-pairs-of-routes): factor "near 1 for pairs the surroundings cannot resolve and
# near 0 beyond", using factor = exp(-N(1-overlap)), N = 1, 10, 100 average scattering times.
import numpy as np
r = np.logspace(-2, 1, 3000); lam = np.linspace(0.7, 1.3, 1201)
om = np.mean(1 - np.sinc(2*r[:, None]/lam[None, :]), axis=1)
ok = True
for N in [1, 10, 100]:
    f = np.exp(-N*om); far = f[r > 2]
    print(f"N={N}: factor for dx/lam>2 ranges {far.min():.3f}..{far.max():.3f}")
    if far.max() > 0.05: ok = False
print("PASS" if ok else "FAIL: after 1 scattering time the factor levels off at 1/e = 0.37, not near 0 (Poisson: e^-1 chance of no scattering)")
