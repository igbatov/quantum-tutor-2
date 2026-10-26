# Claims: DG "54 V", "peak (near 50 deg) close to ... lambda = h/p"; "lambda ∝ 1/sqrt(V0)";
# COW "m g Δz T/hbar", "about ±16 rad", "roughly five fringes", "T=10 µs (~2000 m/s over ~2 cm)",
# "ideal phase is ∝ m^2" at fixed wavelength.
import numpy as np, sympy as sp
from scipy.constants import h,hbar,m_e,e,m_n,c
ok=True
lam=lambda V: h/np.sqrt(2*m_e*e*V)
L=lam(54); print("lambda(54 eV) = %.4f A"%(L*1e10))
Lrel=h/np.sqrt(2*m_e*e*54*(1+e*54/(2*m_e*c**2))); print("relativistic corr: %.2e"%(1-Lrel/L))
ok&=abs(L*1e10-1.67)<0.01
d_surf=2.15e-10   # Ni(111) surface row spacing
phi=np.degrees(np.arcsin(L/d_surf)); print("surface-grating peak angle: %.1f deg (observed ~50)"%phi)
ok&=abs(phi-50)<2
# Bragg planes: d=0.91 A, glancing angle theta, scattering angle 180-2theta
dB=0.91e-10; thB=np.degrees(np.arcsin(L/(2*dB))); print("Bragg glancing %.1f deg -> scattering %.1f deg"%(thB,180-2*thB))
# lambda measured from 50 deg peak:
print("lambda implied by 50 deg on surface grating: %.3f A"%(d_surf*np.sin(np.radians(50))*1e10))
ok&=np.isclose(lam(4*54)/L,0.5)
# COW
v=2000.0; Lpath=0.02; T=Lpath/v; print("T = %.2e s"%T); ok&=np.isclose(T,1e-5)
g=9.8; dz0=0.02; T=1e-5
dphi=lambda ph: m_n*g*dz0*np.sin(np.radians(ph))*T/hbar
edge=dphi(30); print("phase at +30 deg: %.2f rad"%edge); ok&=abs(edge-16)<1
fr=2*edge/(2*np.pi); print("fringes across -30..30: %.2f"%fr); ok&=abs(fr-5)<0.5
# m^2 scaling at fixed wavelength
M,G,DZ,Lp,lm,hb=sp.symbols("m g Dz L lambda hbar",positive=True)
p=2*sp.pi*hb/lm; ph=M*G*DZ*(Lp*M/p)/hb
ok&=sp.simplify(sp.diff(sp.log(ph),M)*M)==2; print("d ln(phase)/d ln m =",sp.simplify(sp.diff(sp.log(ph),M)*M))
# dimensions: m g Δz T / hbar dimensionless (kg m s^-2 m s / (J s))
print("units: kg*m/s^2*m*s/(J*s) -> dimensionless")
print("PASS" if ok else "FAIL")
