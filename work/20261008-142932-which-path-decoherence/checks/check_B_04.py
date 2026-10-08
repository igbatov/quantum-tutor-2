# Claims (fig b-rules-out): "for isotropic recoil the shift is spread uniformly between -0.25 and +0.25
# stripe spacings" at d = lam/4; averaged pattern "visibility sin(pi/2)/(pi/2) ~ 0.64, identical to" record value.
import numpy as np, sympy as sp
rng = np.random.default_rng(0)
n = rng.normal(size=(2_000_000, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
hist, _ = np.histogram(n[:, 0], bins=20, range=(-1, 1), density=True)
unif = np.max(np.abs(hist-0.5)) < 0.01
d_over_lam = 0.25
shift = n[:, 0]*d_over_lam   # phase k*nx*d / 2pi in stripe spacings
print(f"photon x-direction histogram uniform on [-1,1]: {unif}; shift range [{shift.min():.3f},{shift.max():.3f}] stripe spacings")
Vkick = abs(np.mean(np.exp(2j*np.pi*shift)))
Vrec = np.sinc(2*d_over_lam)
x = sp.symbols('x')
Vsym = sp.simplify(sp.integrate(sp.cos(sp.pi/2*x), (x, -1, 1))/2)
print(f"kick-average V = {Vkick:.4f}; record overlap = {Vrec:.4f}; exact = {Vsym} = {float(Vsym):.4f}")
# general d: uniform phase in [-kd, kd] averages to sin(kd)/(kd) exactly
a = sp.symbols('a', positive=True)
gen = sp.simplify(sp.integrate(sp.cos(a*x), (x, -1, 1))/2 - sp.sin(a)/a)
print("general equivalence residual:", gen)
ok = unif and abs(Vkick-Vrec) < 2e-3 and abs(Vrec-0.64) < 0.005 and gen == 0
print("PASS" if ok else "FAIL")
