# Claims (Model 2): "the wave splits into two separating packets ... chances given by the squared sizes";
# "steer its two packets back together ... a later Z magnet gives 'up' every time (ideal; real: nearly)";
# "Models 1 and 2 ... never disagree"
# 1D split-step simulation, hbar=m=1. X magnet: H = p^2/2 - F(t) y sigma_x. Work in sigma_x eigenbasis.
import numpy as np
L,N=400.0,8192; y=np.linspace(-L/2,L/2,N,endpoint=False); dy=y[1]-y[0]
k=2*np.pi*np.fft.fftfreq(N,dy); s0=1.0
phi0=(2*np.pi*s0**2)**-0.25*np.exp(-y**2/(4*s0**2))
def evolve(phi,sign,Fseq,dt):
    for F in Fseq:
        phi=phi*np.exp(1j*sign*F*y*dt/2)
        phi=np.fft.ifft(np.exp(-1j*k**2*dt/2)*np.fft.fft(phi))
        phi=phi*np.exp(1j*sign*F*y*dt/2)
    return phi
F,T,dt=0.5,10.0,0.01; n=int(T/dt)
ok=True
# Model 2 vs Model 1 at several angles: state at polar angle th from +x axis
for th in [0.0,np.pi/3,np.pi/2,2*np.pi/3]:
    cp,cm=np.cos(th/2),np.sin(th/2)
    pp=evolve(cp*phi0,+1,[F]*n,dt); pm=evolve(cm*phi0,-1,[F]*n,dt)
    dens=abs(pp)**2+abs(pm)**2
    Pplus=np.sum(dens[y>0])*dy; overlap=np.sum(abs(pp)*abs(pm))*dy
    print(f"theta={np.degrees(th):5.1f}: weight in +y packet={Pplus:.4f}  Model1 cos^2(th/2)={cp**2:.4f}  packet overlap={overlap:.1e}")
    ok &= abs(Pplus-cp**2)<1e-3
# Full loop: +F for T, -F for 2T, +F for T, starting Z-up = (|+>+|->)/sqrt2
def loop(eps):
    seq=[F]*n+[-F*(1+eps)]*(2*n)+[F]*n
    pp=evolve(phi0/np.sqrt(2),+1,seq,dt); pm=evolve(phi0/np.sqrt(2),-1,seq,dt)
    up=(pp+pm)/np.sqrt(2); return np.sum(abs(up)**2)*dy
mid_sep=2*F*T**2; print("max packet separation",mid_sep,"vs width ~",s0*np.sqrt(1+(2*T/(2*s0**2))**2))
P_ideal=loop(0.0); P_imp=loop(0.002)
print(f"after recombination, P(Z up): ideal={P_ideal:.6f}, with 0.2% force mismatch={P_imp:.4f}")
ok &= abs(P_ideal-1)<1e-6 and 0.5<P_imp<1
print("PASS" if ok else "FAIL")
