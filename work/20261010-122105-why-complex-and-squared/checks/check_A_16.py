# Claims (pilot wave): "a cloud spread as the squared length stays so under the steering; a cloud
# spread as the plain length does not in general"; velocity "set by how fast the hand's angle changes
# from place to place"; "a real wave function (angle constant) would mean a particle at rest".
# Model: 1D free particle, hbar=m=1, psi = sum of two Gaussians at +-2 (two openings), sigma0=0.5.
# In 1D trajectories do not cross, so a density rho is carried along iff its cumulative fraction to
# the left of each trajectory is constant in time.
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp, cumulative_trapezoid
X, T = sp.symbols('x t', real=True); s0 = sp.Rational(1, 2)
def g(c):
    a = s0**2 + sp.I*T/2
    return (2*sp.pi)**sp.Rational(-1, 4)*sp.sqrt(s0)/sp.sqrt(a)*sp.exp(-(X-c)**2/(4*a))
psi_s = g(2) + g(-2)
schr = sp.simplify(sp.I*sp.diff(psi_s, T) + sp.diff(psi_s, X, 2)/2)
ok_schr = schr == 0
psi = sp.lambdify((X, T), psi_s, 'numpy'); dpsi = sp.lambdify((X, T), sp.diff(psi_s, X), 'numpy')
vel = lambda t, x: np.imag(dpsi(x, t)/psi(x, t))       # v = (hbar/m) dS/dx
# real psi -> v = 0
ok_real = abs(np.imag(dpsi(0.7, 0.0)/psi(0.7, 0.0))) < 1e-14
xs = np.linspace(-30, 30, 120001)
def cdf(rho):
    c = cumulative_trapezoid(rho, xs, initial=0); return c/c[-1]
tf = 6.0
P0, Pf = abs(psi(xs, 0.0)), abs(psi(xs, tf))
starts = np.linspace(-3.2, 3.2, 33)
ends = []
for x0 in starts:
    sol = solve_ivp(vel, (0, tf), [x0], rtol=1e-11, atol=1e-12, method='DOP853'); ends.append(sol.y[0, -1])
ends = np.array(ends)
res = {}
for name, k in (('squared length', 2), ('plain length', 1)):
    F0 = np.interp(starts, xs, cdf(P0**k)); Ff = np.interp(ends, xs, cdf(Pf**k))
    res[name] = np.max(abs(F0 - Ff))
print('Schrodinger satisfied:', ok_schr, '| real psi gives v=0:', ok_real)
print('max change of carried fraction along trajectories:', {k: f'{v:.2e}' for k, v in res.items()})
ok = ok_schr and ok_real and res['squared length'] < 1e-4 and res['plain length'] > 1e-2
print('PASS' if ok else 'FAIL')
