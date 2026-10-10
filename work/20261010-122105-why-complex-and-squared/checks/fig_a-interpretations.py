# Pilot-wave steering for psi = two spreading Gaussians (hbar = m = 1, sigma0 = 0.5, centres +-2).
# Left: trajectories over |psi|^2. Right: at t = 6, an ensemble started as |psi0|^2 (top) still
# matches |psi_t|^2; an ensemble started as normalised |psi0| (bottom) no longer matches |psi_t|.
import numpy as np, sympy as sp, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, cumulative_trapezoid
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-interpretations.png'
plt.rcParams.update({'font.size': 10})
X, T = sp.symbols('x t', real=True); s0 = sp.Rational(1, 2)
def g(c):
    a = s0**2 + sp.I*T/2
    return (2*sp.pi)**sp.Rational(-1, 4)*sp.sqrt(s0)/sp.sqrt(a)*sp.exp(-(X-c)**2/(4*a))
ps = g(2) + g(-2)
psi = sp.lambdify((X, T), ps, 'numpy'); dpsi = sp.lambdify((X, T), sp.diff(ps, X), 'numpy')
vel = lambda t, x: np.imag(dpsi(x, t)/psi(x, t))
tf = 6.0; xs = np.linspace(-25, 25, 50001)
def sample(rho, n):
    c = cumulative_trapezoid(rho, xs, initial=0); c /= c[-1]
    return np.interp((np.arange(n)+0.5)/n, c, xs)
def evolve(x0):
    return np.array([solve_ivp(vel, (0, tf), [x], rtol=1e-8, atol=1e-10, method='DOP853').y[0, -1] for x in x0])
n = 1500
e2 = evolve(sample(abs(psi(xs, 0))**2, n)); e1 = evolve(sample(abs(psi(xs, 0)), n))
fig = plt.figure(figsize=(10, 4.6))
a = fig.add_axes([0.07, 0.12, 0.40, 0.78])
tt = np.linspace(0, tf, 200); XX, TT = np.meshgrid(np.linspace(-12, 12, 600), tt)
a.pcolormesh(XX, TT, abs(psi(XX, TT))**2, cmap='Greys', shading='auto', vmax=0.25)
for x0 in sample(abs(psi(xs, 0))**2, 40):
    sol = solve_ivp(vel, (0, tf), [x0], rtol=1e-8, atol=1e-10, dense_output=True, method='DOP853')
    a.plot(sol.sol(tt)[0], tt, color='tab:blue', lw=0.7)
a.set_xlim(-12, 12); a.set_xlabel('position x (units with \u0127 = m = 1; packets of width 0.5 at \u00b12)'); a.set_ylabel('time t (same units)')
a.set_title('Trajectories steered by the hand\'s angle\n(shading: squared length |ψ|²)', fontsize=10)
bins = np.linspace(-12, 12, 121)
r2 = abs(psi(xs, tf))**2; r2 /= np.trapezoid(r2, xs); r1 = abs(psi(xs, tf)); r1 /= np.trapezoid(r1, xs)
b1 = fig.add_axes([0.56, 0.56, 0.42, 0.34]); b2 = fig.add_axes([0.56, 0.12, 0.42, 0.34])
b1.hist(e2, bins=bins, density=True, color='0.75', edgecolor='0.5', label='ensemble started as |ψ₀|²')
b1.plot(xs, r2, 'k-', lw=1.6, label='|ψ_t|² (normalised)'); b1.set_xlim(-12, 12); b1.legend(fontsize=8, loc='upper right')
b1.set_title('at t = 6: squared-length cloud stays squared-length', fontsize=9.5); b1.set_ylabel('density')
b2.hist(e1, bins=bins, density=True, color='0.75', edgecolor='0.5', label='ensemble started as |ψ₀| (normalised)')
b2.plot(xs, r1, 'k--', lw=1.6, label='|ψ_t| (normalised)'); b2.set_xlim(-12, 12); b2.legend(fontsize=8, loc='upper right')
b2.set_title('at t = 6: plain-length cloud does not stay plain-length', fontsize=9.5); b2.set_ylabel('density'); b2.set_xlabel('position x')
for bb in (b1, b2): bb.set_ylim(0, 0.4)
fig.savefig(out, dpi=150)
# quantitative mismatch (total variation distance between histogram and curve)
def tv(e, r):
    h, edges = np.histogram(e, bins=bins, density=True); mids = (edges[:-1]+edges[1:])/2
    return 0.5*np.sum(abs(h - np.interp(mids, xs, r)))*(edges[1]-edges[0])
print('saved', out, '| TV distance squared-cloud:', round(tv(e2, r2), 3), ' plain-cloud:', round(tv(e1, r1), 3))
