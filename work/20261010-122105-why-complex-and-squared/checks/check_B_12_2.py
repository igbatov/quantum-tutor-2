# Claims (pilot-wave): "a cloud distributed as |psi|^2 at one moment is distributed as |psi|^2 for ever";
# d sqrt(rho)/dt "= -(sqrt(rho) v)' + 1/2 sqrt(rho) v'"; "dN/dt = 1/2 int sqrt(rho) v' dx";
# "d sigma/dt = -(sigma v)' + 1/2 sigma (v' - <v'>)"; "vanishes only when dv/dx is the same everywhere ... as for one
# freely spreading Gaussian"; "for two overlapping packets ... the |psi| cloud drifts away"; caption "exact density
# there is about 0.48" (two packets, t = 4, x = 0).
import sympy as sp, numpy as np
x, t = sp.symbols('x t', real=True)
rho = sp.Function('rho', positive=True)(x, t); v = sp.Function('v', real=True)(x, t); N = sp.Function('N', positive=True)(t)
rt = -sp.diff(rho*v, x)
ok = sp.simplify(rt/(2*sp.sqrt(rho)) - (-sp.diff(sp.sqrt(rho)*v, x) + sp.sqrt(rho)*sp.diff(v, x)/2)) == 0
# sigma = sqrt(rho)/N with N' = 1/2 int sqrt(rho) v' = (N/2) <v'>, so d sigma/dt = (d sqrt rho/dt)/N - sigma N'/N
vbar = sp.symbols('vbar', real=True)   # <v'>
sig = sp.sqrt(rho)/N
dsig = (-sp.diff(sp.sqrt(rho)*v, x) + sp.sqrt(rho)*sp.diff(v, x)/2)/N - sig*(N*vbar/2)/N
ok &= sp.simplify(dsig - (-sp.diff(sig*v, x) + sig*(sp.diff(v, x) - vbar)/2)) == 0
print("symbolic steps:", ok)
# Numerics: free particle hbar = m = 1; Bohm flow map is fixed by equivariance: F_t(X_t(x0)) = F_0(x0) (|psi|^2 CDFs)
L, Nx = 160.0, 2**14
X = np.linspace(-L/2, L/2, Nx, endpoint=False); dx = X[1]-X[0]; K = 2*np.pi*np.fft.fftfreq(Nx, dx)
ev = lambda p0, tt: np.fft.ifft(np.exp(-0.5j*K**2*tt)*np.fft.fft(p0))
g = lambda c: np.exp(-(X-c)**2/4)    # |psi|^2 has std 1 = "initial packet width"
def vel(psi):
    d = np.fft.ifft(1j*K*np.fft.fft(psi)); return np.imag(np.conj(psi)*d)/np.maximum(np.abs(psi)**2, 1e-300)
def test(psi0, T=4.0, n=4000, steps=400):
    psi0 = psi0/np.sqrt((np.abs(psi0)**2).sum()*dx)
    out = {}
    for name, w in [("sq", np.abs(psi0)**2), ("abs", np.abs(psi0))]:
        F = np.cumsum(w); F /= F[-1]; P = np.interp((np.arange(n)+0.5)/n, F, X); dt = T/steps; tt = 0
        for _ in range(steps):
            f = lambda p, s: np.interp(p, X, vel(ev(psi0, s)))
            k1 = f(P, tt); k2 = f(P+dt/2*k1, tt+dt/2); k3 = f(P+dt/2*k2, tt+dt/2); k4 = f(P+dt*k3, tt+dt)
            P = P + dt/6*(k1+2*k2+2*k3+k4); tt += dt
        pT = ev(psi0, T); tgt = np.abs(pT)**2 if name == "sq" else np.abs(pT); Ft = np.cumsum(tgt); Ft /= Ft[-1]
        out[name] = np.abs(np.searchsorted(np.sort(P), X)/n - Ft).max()
    # exact |psi|-cloud density at x = 0 via the equivariant flow map: sigma_t(x) = rho_t(x) / (|psi0(x0)| N0)
    r0, rT = np.abs(psi0)**2, np.abs(ev(psi0, T))**2
    F0, FT = np.cumsum(r0)*dx, np.cumsum(rT)*dx; i0 = np.argmin(np.abs(X)); x0 = np.interp(FT[i0], F0, X)
    N0 = np.abs(psi0).sum()*dx
    out["sigma(0)"] = rT[i0]/(np.interp(x0, X, np.abs(psi0))*N0)
    out["|psi_T|(0)/N_T"] = np.sqrt(rT[i0])/(np.sqrt(rT).sum()*dx)
    return out
one = test(g(0).astype(complex)); two = test((g(-3)+g(3)).astype(complex))
print("one Gaussian:", {k: round(v, 4) for k, v in one.items()})
print("two packets :", {k: round(v, 4) for k, v in two.items()})
ok &= one["sq"] < 0.01 and two["sq"] < 0.01 and one["abs"] < 0.01 and two["abs"] > 0.03
ok &= abs(two["sigma(0)"] - 0.48) < 0.02
print("PASS" if ok else "FAIL")
