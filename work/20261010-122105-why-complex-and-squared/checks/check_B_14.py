# Claims (pilot-wave): "a cloud distributed as |psi|^2 at one moment is distributed as |psi|^2 for
#  ever"; "A cloud distributed as |psi| = sqrt(rho) is not: it would need d sqrt(rho)/dt =
#  -d(sqrt(rho) v)/dx ... differs ... by 1/2 sqrt(rho) dv/dx, zero only where the velocity field is
#  uniform".
# (a) symbolic: the stated difference.  (b) physical: a NORMALISED cloud proportional to |psi| needs
# d(sqrt(rho)/N)/dt = -d(sqrt(rho) v/N)/dx with N(t) = int |psi| dx; this holds iff dv/dx = 2 N'/N,
# i.e. dv/dx the same at every x (pure stretching), not dv/dx = 0.  Test with Bohmian trajectories:
# single free Gaussian (pure stretching) and two overlapping free packets.
import sympy as sp
import numpy as np
x, t = sp.symbols('x t', real=True)
rho = sp.Function('rho', positive=True)(x, t); v = sp.Function('v', real=True)(x, t)
drho = -sp.diff(rho*v, x)
lhs = drho/(2*sp.sqrt(rho))
need = -sp.diff(sp.sqrt(rho)*v, x)
diff = sp.simplify(lhs - need)
print("d sqrt(rho)/dt - [-(sqrt(rho) v)'] =", diff)
sym_ok = sp.simplify(diff - sp.sqrt(rho)*sp.diff(v, x)/2) == 0

L, Nx = 160.0, 8192
X = np.linspace(-L/2, L/2, Nx, endpoint=False); dx = X[1]-X[0]
K = 2*np.pi*np.fft.fftfreq(Nx, dx)
def evolve(psi0, tt):  # hbar = m = 1, free
    return np.fft.ifft(np.exp(-0.5j*K**2*tt)*np.fft.fft(psi0))
def vel(psi):
    dpsi = np.fft.ifft(1j*K*np.fft.fft(psi))
    return np.imag(np.conj(psi)*dpsi)/np.maximum(np.abs(psi)**2, 1e-300)
def quantile_points(w, n):
    F = np.cumsum(w); F /= F[-1]
    return np.interp((np.arange(n)+0.5)/n, F, X)
def ks(points, w):
    F = np.cumsum(w); F /= F[-1]
    Fe = np.searchsorted(np.sort(points), X)/len(points)
    return np.abs(Fe - F).max()
def run(psi0, Tend, nsteps=800, n=3000):
    res = {}
    for name, w0 in [("|psi|^2", np.abs(psi0)**2), ("|psi|", np.abs(psi0))]:
        P = quantile_points(w0, n); dt = Tend/nsteps; tt = 0.0
        for _ in range(nsteps):  # RK4 with exact psi at each stage
            def f(p, s): return np.interp(p, X, vel(evolve(psi0, s)))
            k1 = f(P, tt); k2 = f(P+dt/2*k1, tt+dt/2); k3 = f(P+dt/2*k2, tt+dt/2); k4 = f(P+dt*k3, tt+dt)
            P = P + dt/6*(k1+2*k2+2*k3+k4); tt += dt
        psiT = evolve(psi0, Tend)
        target = np.abs(psiT)**2 if name == "|psi|^2" else np.abs(psiT)
        res[name] = ks(P, target)
    return res
g = lambda c, s: np.exp(-(X-c)**2/(4*s**2))
single = g(0, 1.0).astype(complex); single /= np.sqrt((np.abs(single)**2).sum()*dx)
two = (g(-3, 1.0) + g(3, 1.0)).astype(complex); two /= np.sqrt((np.abs(two)**2).sum()*dx)
r1 = run(single, 4.0, nsteps=200); r2 = run(two, 4.0)
print("single Gaussian, KS distance of transported cloud from target at t=4:", r1)
print("two packets,     KS distance of transported cloud from target at t=4:", r2)
eq_ok = r1["|psi|^2"] < 0.01 and r2["|psi|^2"] < 0.01
not_eq_two = r2["|psi|"] > 0.03
gauss_kept = r1["|psi|"] < 0.01
print("symbolic difference 1/2 sqrt(rho) v':", "PASS" if sym_ok else "FAIL")
print("|psi|^2 equivariance:", "PASS" if eq_ok else "FAIL")
print("|psi| cloud not preserved for two packets:", "PASS" if not_eq_two else "FAIL")
print("Claim 'cloud ~ |psi| is not preserved; equality only where velocity field uniform':",
      "FAIL (a single spreading Gaussian keeps a |psi|-distributed cloud |psi|-distributed, although dv/dx != 0)"
      if gauss_kept else "PASS")
