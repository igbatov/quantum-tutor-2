# Claims (Model 2 and its figure): "turns by (momentum x distance)/hbar ... once per de Broglie wavelength";
# "longer than the straight route by about y^2/D"; "y = 1 means an extra quarter wavelength";
# "hands near the classical path line up, the rest cancel"; far routes "contribute far less per unit of y".
import numpy as np
hb = 1.0; p = 2.7; lam = 2*np.pi*hb/p
ok = abs(p*lam/hb - 2*np.pi) < 1e-12
D = 1000.0; y = np.linspace(0, 30, 7)
extra = 2*np.sqrt(D**2+y**2) - 2*D
print("extra / (y^2/D):", np.round(extra/(y**2/D), 5)); ok &= np.all(np.abs(extra[1:]/(y[1:]**2/D)-1) < 1e-3)
# Fresnel units: phase = (pi/2) u^2 -> at u=1 phase = pi/2 = quarter turn = quarter wavelength of extra path
ok &= abs(0.5*np.pi*1**2 - 2*np.pi*0.25) < 1e-12
u = np.linspace(-6, 6, 240001); du = u[1]-u[0]; h = np.exp(0.5j*np.pi*u**2)
near = abs(h[np.abs(u) <= 1].sum()*du)/2
far = abs(h[(u > 5) & (u < 6)].sum()*du)/1
print(f"|sum| per unit y: |u|<=1: {near:.3f}; 5<u<6: {far:.3f}; total {abs(h.sum()*du):.3f} vs ideal sqrt2 {np.sqrt(2):.3f}")
ok &= near > 0.85 and far < 0.1
print("PASS" if ok else "FAIL")
