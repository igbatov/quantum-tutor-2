# Claims (pilot wave): "goes through one slit on a definite bent path, kept away from the dark lines,
# and chance comes only from not knowing its exact starting point" (i.e. same pattern as |psi|^2).
import numpy as np
from scipy.integrate import solve_ivp
from scipy.stats import kstest
sig, x0 = 0.3, 3.0   # two Gaussian "slits" at +-3 (hbar = m = 1), transverse motion only
def psi_dpsi(x, t):
    s = 1 + 1j*t/(2*sig**2)
    out = 0; dout = 0
    for c in (-x0, x0):
        g = (2*np.pi*sig**2)**-0.25 * s**-0.5 * np.exp(-(x-c)**2/(4*sig**2*s))
        out = out + g; dout = dout + g*(-(x-c)/(2*sig**2*s))
    return out/np.sqrt(2), dout/np.sqrt(2)
def vel(t, x):
    p, dp = psi_dpsi(x, t); return np.imag(dp/p)
rng = np.random.default_rng(1)
N = 3000
xi = np.concatenate([rng.normal(-x0, sig, N//2), rng.normal(x0, sig, N//2)])
T = 30.0
sol = solve_ivp(vel, (0, T), xi, rtol=1e-9, atol=1e-9, t_eval=np.linspace(0, T, 301), method='DOP853')
xt = sol.y
crossed = np.sum(np.any(np.sign(xt) != np.sign(xi)[:, None], axis=1))
print("trajectories that cross the symmetry line (switch sides):", crossed)
# equivariance: final positions distributed as |psi(T)|^2 -> KS test against numerical CDF
grid = np.linspace(-250, 250, 200001)
rho = np.abs(psi_dpsi(grid, T)[0])**2; cdf = np.cumsum(rho); cdf /= cdf[-1]
stat, pval = kstest(xt[:, -1], lambda x: np.interp(x, grid, cdf))
print(f"KS test final positions vs |psi|^2: D={stat:.4f}, p={pval:.3f}")
# dark lines: minima of |psi(T)|^2 ; count trajectories within +-0.5 of each minimum vs expectation
from scipy.signal import argrelmin
mins = grid[argrelmin(rho)[0]]; mins = mins[abs(mins) < 120]
rhomax = rho.max()
print("dark-line positions:", np.round(mins, 1), " min density/peak:", np.round(np.interp(mins, grid, rho)/rhomax, 6))
near = sum(np.sum(abs(xt[:, -1]-m) < 0.5) for m in mins)
expct = N*sum(np.interp(m+0.5, grid, cdf)-np.interp(m-0.5, grid, cdf) for m in mins)
print(f"trajectories ending within 0.5 of a dark line: {near} (|psi|^2 predicts {expct:.2f})")
ok = crossed == 0 and pval > 0.01 and near <= max(3, 3*expct)
print("PASS" if ok else "FAIL")
