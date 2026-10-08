# Claims (Hackermueller 2004): an emitted photon's tag "overlap[s] almost completely if its wavelength
# is much longer than the path separation, and little or not at all once it is shorter than about
# twice the separation"; "a hotter molecule sends off more photons, and shorter ones".
import numpy as np
from scipy.integrate import quad
from scipy.constants import h, c, k
# overlap of the two emitted-photon states = <exp(i k.d)> over emission directions
iso = lambda x: np.sinc(x/np.pi)                       # sin(x)/x
def dipole(x, axis):                                   # dipole pattern, dipole randomly oriented -> isotropic; fixed dipole:
    f = lambda ct: (np.cos(x*ct) * (1-ct**2) if axis == "par" else np.cos(x*ct)*(1+ct**2)/2)
    return quad(f, -1, 1)[0]/quad(lambda ct: (1-ct**2) if axis == "par" else (1+ct**2)/2, -1, 1)[0]
ok = True
for r in [20, 10, 4, 2, 1.5, 1.2, 1, 0.7, 0.5]:      # lambda / d
    x = 2*np.pi/r
    vals = [iso(x), dipole(x, "par"), dipole(x, "perp")]
    print(f"lambda = {r:4.1f} d: overlap isotropic {vals[0]:+.3f}, dipole || d {vals[1]:+.3f}, dipole perp d {vals[2]:+.3f}")
    if r >= 20: ok &= min(vals) > 0.95
    if r == 10: ok &= min(vals) > 0.9
    if r <= 2: ok &= abs(vals[0]) < 0.25 and max(abs(v) for v in vals) < 0.35   # random orientation -> isotropic; fixed dipole as worst case
# thermal emission: photon-number spectrum ~ sigma_abs(nu) * nu^2 / (exp(h nu/kT)-1), sigma ~ nu (graybody-like)
d = 1e-6
def spec(nu, T): return nu**3/np.expm1(h*nu/(k*T))
for T in [1000, 2000, 3000]:
    tot = quad(spec, 1e11, 3e15, args=(T,), limit=200)[0]
    short = quad(spec, c/(2*d), 3e15, args=(T,), limit=200)[0]
    print(f"T = {T} K: relative photon emission rate {tot/quad(spec,1e11,3e15,args=(1000,),limit=200)[0]:6.1f}; fraction with lambda < 2d (2 um): {short/tot:.2f}; Wien peak {2.898e-3/T*1e6:.2f} um")
print("(spectral model is illustrative: graybody with absorption ~ nu; real C70 emissivity differs)")
xs = np.linspace(2*np.pi/2, 2*np.pi/0.1, 20000); print(f"max |sinc| for lambda <= 2d: {np.max(np.abs(iso(xs))):.3f}")
print("PASS" if ok else "FAIL")
