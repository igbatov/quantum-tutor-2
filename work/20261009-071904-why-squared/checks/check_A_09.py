# Claim (pilot-wave): "if positions are spread according to the squared size ... the steering
# keeps them spread that way for ever, while ... plain size or the cube would not in general"
# Test: 1D free particle (hbar = m = 1), superposition of two Gaussian packets.
# Equivariance <=> continuity residual R = d_t rho + d_x(rho v) = 0, rho = |psi|^p / N_p(t),
# v = Im(psi_x / psi) (guidance law).
import numpy as np, sympy as sp
x, t = sp.symbols('x t', real=True)
def packet(x0, k, s=sp.Rational(1)):
    a = 1 + sp.I*t/(2*s**2)
    return a**sp.Rational(-1, 2)*sp.exp(-(x - x0 - k*t)**2/(4*s**2*a) + sp.I*k*(x - x0) - sp.I*k**2*t/2)
psi = packet(-4, 2) + packet(4, -2)
schr = sp.I*sp.diff(psi, t) + sp.diff(psi, x, 2)/2
f_s = sp.lambdify((x, t), schr, 'numpy')
f_psi = sp.lambdify((x, t), psi, 'numpy'); f_px = sp.lambdify((x, t), sp.diff(psi, x), 'numpy')
f_pt = sp.lambdify((x, t), sp.diff(psi, t), 'numpy')
X = np.linspace(-20, 20, 40001); dx = X[1] - X[0]
print("Schrodinger residual max:", np.max(np.abs(f_s(X, 1.3))))
def residual(p, T):
    ps, px, pt = f_psi(X, T), f_px(X, T), f_pt(X, T)
    A = np.abs(ps)
    v = np.imag(px/ps)
    dA_dt = np.real(np.conj(ps)*pt)/A                     # d|psi|/dt
    u = A**p; du_dt = p*A**(p-1)*dA_dt
    N = np.sum(u)*dx; dN_dt = np.sum(du_dt)*dx
    rho = u/N; drho_dt = du_dt/N - u*dN_dt/N**2
    flux = rho*v
    R = drho_dt + np.gradient(flux, dx)
    return np.max(np.abs(R))/np.max(np.abs(drho_dt))
ok = True
Ts = np.linspace(0.25, 3.0, 12)
for p in (1, 2, 3):
    rs = [residual(p, T) for T in Ts]
    print(f"p={p}: relative continuity residual over t in [0.25,3]: min={min(rs):.2e}, max={max(rs):.2e}")
    if p == 2: ok &= max(rs) < 1e-4
    else: ok &= max(rs) > 1e-2      # violated at some time => not preserved
print("PASS" if ok else "FAIL")
