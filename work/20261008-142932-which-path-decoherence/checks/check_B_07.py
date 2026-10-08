# Claims (Experiment 3): "At 1,000 K hardly any emitted photons are that short" (< 2 um);
# "by 3,000 K ... emits visible and near-infrared photons"; emission "both grows and shifts to shorter
# wavelengths, so the number of photons ... left of the 2-micrometre line rises steeply". (Black-body idealization.)
import numpy as np
from scipy import constants as C
from scipy.integrate import quad
hc_k = C.h*C.c/C.k
def nphot(lam, T):  # photons per unit wavelength per unit time per area (relative)
    return 2*C.c/lam**4/np.expm1(hc_k/(lam*T))
def frac(T, lmax, lmin=1e-8):
    tot = quad(nphot, 1e-8, 1e-2, args=(T,), limit=500, points=[hc_k/T/3.92])[0]
    return quad(nphot, lmin, lmax, args=(T,), limit=500)[0]/tot, tot
res = {}
for T in [1000, 2000, 3000]:
    f2, tot = frac(T, 2e-6); fv, _ = frac(T, 0.75e-6); res[T] = (f2, tot)
    lpk = hc_k/T/3.9207   # photon-number peak per unit wavelength
    print(f"T={T} K: frac photons <2um = {f2:.4f}, <0.75um (visible) = {fv:.2e}, photon-peak wavelength = {lpk*1e6:.2f} um, total rate (rel) = {tot/res[1000][1]:.1f}")
r = res[3000][0]*res[3000][1]/(res[1000][0]*res[1000][1])
print(f"rate of <2um photons, 3000K / 1000K = {r:.0f}")
# hotter curve higher everywhere?
lam = np.logspace(np.log10(0.3e-6), -5, 400)
higher = np.all(nphot(lam, 3000) > nphot(lam, 2000)) and np.all(nphot(lam, 2000) > nphot(lam, 1000))
print("hotter curves higher at every wavelength:", higher)
ok = res[1000][0] < 0.05 and r > 100 and higher
print("PASS" if ok else "FAIL")
