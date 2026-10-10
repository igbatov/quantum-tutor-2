# Claim: "the counts oscillate smoothly with a period of 720° of spin rotation"; 360° reverses sign, 720° restores
import numpy as np
th=np.linspace(0,8*np.pi,4001)
amp_rot=np.cos(th/2)  # <up| exp(-i th sigma_z/2)... relative phase factor e^{-i th/2} on spin-up neutrons: interference with unrotated beam
I=np.abs(1+np.exp(-1j*th/2))**2/4
# period: smallest T>0 with I(th+T)=I(th)
f=lambda T: np.max(np.abs(np.abs(1+np.exp(-1j*(th+T)/2))**2/4-I))
print('I(360deg)=',I[np.argmin(abs(th-2*np.pi))],' I(720deg)=',I[np.argmin(abs(th-4*np.pi))],' period 2pi ok?',f(2*np.pi)<1e-12,' period 4pi ok?',f(4*np.pi)<1e-12)
ok = f(4*np.pi)<1e-12 and f(2*np.pi)>0.5 and np.all(np.diff(I)!=np.nan)
print('PASS' if ok else 'FAIL')
