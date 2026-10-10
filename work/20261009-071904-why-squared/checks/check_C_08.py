# Claim (pilot-wave): a cloud "spread out as the squared size of the wave is carried ... into
# ... the squared size of the later wave"; "plain size or the cube is, in general, carried into
# something else".  Test: continuity equation d(rho)/dt + d(rho v)/dx = 0 with the guidance
# velocity v = Im(psi_x/psi) (hbar = m = 1), for rho_p = |psi|^p / integral(|psi|^p), on a free
# 1D superposition of two colliding Gaussian packets (interference present).
import numpy as np, sympy as sp
x,t = sp.symbols('x t', real=True)
s0, k0, x0 = 1.0, 2.0, 4.0
def packet(xc, k):
    st = 1 + sp.I*t/(2*s0**2)
    return (2*sp.pi*s0**2)**sp.Rational(-1,4)/sp.sqrt(st)*sp.exp(-(x-xc-k*t)**2/(4*s0**2*st) + sp.I*k*(x-xc) - sp.I*k**2*t/2)
psi = packet(-x0, k0) + 0.7*packet(x0, -k0)
psi_t, psi_x, psi_xx = sp.diff(psi,t), sp.diff(psi,x), sp.diff(psi,x,2)
schr = sp.lambdify((x,t), sp.I*psi_t + psi_xx/2, 'numpy')
F = {n: sp.lambdify((x,t), e, 'numpy') for n,e in [('psi',psi),('pt',psi_t),('px',psi_x)]}
X = np.linspace(-25, 25, 200001); dx = X[1]-X[0]
ok = True
print("Schroedinger residual check:", np.abs(schr(X, 1.3)).max())
ok &= np.abs(schr(X,1.3)).max() < 1e-10
for T in [1.0, 2.0]:
    ps, pt, px = F['psi'](X,T), F['pt'](X,T), F['px'](X,T)
    r2 = np.abs(ps)**2
    j = np.imag(np.conj(ps)*px)                 # = |psi|^2 v
    dr2dt = 2*np.real(np.conj(ps)*pt)
    print(f"t={T}: min |psi|^2 on grid {r2.min():.2e}")
    for p in [1,2,3]:
        Np = np.sum(r2**(p/2))*dx
        # dN/dt = integral of d|psi|^p/dt
        dNp = np.sum((p/2)*r2**(p/2-1)*dr2dt)*dx
        rho = r2**(p/2)/Np
        drho_dt = (p/2)*r2**(p/2-1)*dr2dt/Np - rho*dNp/Np
        flux = r2**(p/2-1)*j/Np                   # rho_p * v
        dflux = np.gradient(flux, dx)
        R = drho_dt + dflux
        m = slice(1000,-1000)
        rel = np.sum(np.abs(R[m]))/np.sum(np.abs(drho_dt[m]))
        print(f"   p={p}: |continuity residual| / |d rho/dt| = {rel:.2e}")
        if p==2: ok &= rel < 1e-4
        else: ok &= rel > 1e-2
print("PASS" if ok else "FAIL")
