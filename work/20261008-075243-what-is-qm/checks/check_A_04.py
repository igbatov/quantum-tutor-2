# Claim: "faster electrons give narrower stripes"; "wavelength is set by the electron's speed (faster, shorter)"
import sympy as sp, numpy as np
from scipy.constants import h, m_e, c, e
v, L, d, m = sp.symbols('v L d m', positive=True)
gamma = 1/sp.sqrt(1 - v**2/sp.Symbol('c', positive=True)**2)
lam = h/(gamma*m*v)  # relativistic de Broglie
spacing = lam*L/d
dS = sp.diff(spacing.subs(sp.Symbol('c', positive=True), c), v)
# sign check numerically over v in (1e3, 0.99c)
vs = np.logspace(3, np.log10(0.99*c), 200)
f = sp.lambdify(v, dS.subs({m: m_e, L: 1.0, d: 1e-6}))
neg = np.all(np.array([f(x) for x in vs]) < 0)
# example: 50 keV vs 100 keV electrons
def lam_E(E):
    p = np.sqrt((E*e)**2 + 2*E*e*m_e*c**2)/c
    return h/p
print(f"lambda(50 keV)={lam_E(50e3)*1e12:.2f} pm, lambda(100 keV)={lam_E(100e3)*1e12:.2f} pm")
print("d(spacing)/dv < 0 for all tested speeds:", neg)
print("PASS" if neg and lam_E(100e3) < lam_E(50e3) else "FAIL")
