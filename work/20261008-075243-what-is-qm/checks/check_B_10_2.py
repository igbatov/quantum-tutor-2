# Round 2 claim (pilot-wave): "which one is fixed by exactly where in the beam it started" ... "No up/down label is involved"
# Bohmian trajectories in a 1D Stern-Gerlach model, hbar=m=1: H = p^2/2 - F z sigma_z.
import numpy as np
from scipy.stats import norm
L,N=200.0,4096; z=np.linspace(-L/2,L/2,N,endpoint=False); dz=z[1]-z[0]
k=2*np.pi*np.fft.fftfreq(N,dz); s0=1.0
phi0=(2*np.pi*s0**2)**-0.25*np.exp(-z**2/(4*s0**2))
F,T,dt=0.5,10.0,0.005; n=int(T/dt)
def run(pu):
    a,b=np.sqrt(pu)*phi0.astype(complex),np.sqrt(1-pu)*phi0.astype(complex)
    # initial positions: equally spaced quantiles of |psi0|^2 (same for any pu: density = phi0^2)
    q=(np.arange(400)+0.5)/400; zs=norm.ppf(q,scale=s0)   # |psi0|^2 is a normal pdf with sd s0
    zt=zs.copy()
    def vel(a,b,x):
        num=np.imag(np.conj(a)*np.gradient(a,dz)+np.conj(b)*np.gradient(b,dz))
        den=abs(a)**2+abs(b)**2+1e-300
        return np.interp(x,z,num/den)
    ex=np.exp(-1j*k**2*dt/2)
    for _ in range(n):
        v1=vel(a,b,zt)
        a=a*np.exp(1j*F*z*dt/2); b=b*np.exp(-1j*F*z*dt/2)
        a=np.fft.ifft(ex*np.fft.fft(a)); b=np.fft.ifft(ex*np.fft.fft(b))
        a=a*np.exp(1j*F*z*dt/2); b=b*np.exp(-1j*F*z*dt/2)
        v2=vel(a,b,zt+v1*dt)
        zt=zt+0.5*(v1+v2)*dt     # Heun step
    return zs,zt
ok=True
for pu in [0.5,0.75]:
    zs,zt=run(pu); up=zt>0
    mono=np.all(np.diff(zt)>0)             # trajectories never cross: outcome set by start position
    thresh_start=zs[~up].max() if (~up).any() else None
    print(f"P(up)={pu}: fraction of trajectories ending up={up.mean():.3f}; order preserved={mono}; "
          f"all starts above z*={zs[up].min():.3f} go up, below go down (z* expected quantile {norm.ppf(1-pu,scale=s0):.3f})")
    ok &= mono and abs(up.mean()-pu)<0.01 and np.all(up==(zs>thresh_start))
print("same start position gives same outcome; spin input only through the wave (no stored label)")
print("PASS" if ok else "FAIL")
