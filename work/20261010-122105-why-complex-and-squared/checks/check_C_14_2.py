# Claim: "a cloud spread as |psi|^2 stays so for ever under the steering law (equivariance),
# while a cloud spread as |psi| or |psi|^4 does not in general"
# Test: 1D free particle (hbar=m=1), psi = sum of two Gaussian packets. Bohm velocity v = Im(psi'/psi).
# For rho = |psi|^p / N(t): drho/dt + d(rho v)/dx = 0 must hold for all x and t if the shape is kept.
import numpy as np
x=np.linspace(-15,15,30001); dx=x[1]-x[0]
def g(x,t,x0,k0,s=1.0):
    st=s*(1+1j*t/(2*s**2))
    return np.exp(-(x-x0-k0*t)**2/(4*s*st)+1j*k0*(x-x0-k0*t/2))/np.sqrt(st)
psi=lambda t: g(x,t,-3,1.5)+g(x,t,3,-1.5)
def residual(p,t,dt=1e-4):
    def rho(tt):
        r=np.abs(psi(tt))**p; return r/(r.sum()*dx)
    ps=psi(t); v=np.imag(np.gradient(ps,dx)/ps)
    drdt=(rho(t+dt)-rho(t-dt))/(2*dt); flux=np.gradient(rho(t)*v,dx)
    m=np.abs(x)<8; return np.abs(drdt+flux)[m].max()/rho(t)[m].max()
ok=True
for t in (0.5,1.5):
    r={p:residual(p,t) for p in (1,2,4)}; print("t",t,{p:f"{val:.2e}" for p,val in r.items()})
    ok&=r[2]<1e-3 and r[1]>1e-2 and r[4]>1e-2
# single Gaussian (linear velocity field): |psi|^4 is also kept -> "in general" is the right qualifier
psi=lambda t: g(x,t,0,0.0); r4=residual(4,1.0); print("single Gaussian, p=4 residual:",f"{r4:.1e}")
print("PASS" if ok else "FAIL")
