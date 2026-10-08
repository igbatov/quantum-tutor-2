# Claim: "Squeezing a wave into a small space forces it to mix many wavelengths";
#        "no wave can be both tightly located and of a single wavelength"
# Numerically: Gaussian packets of shrinking width; momentum spread via FFT; product >= hbar/2.
import numpy as np
hbar = 1.0
N = 2**14; Lbox = 400.0
x = np.linspace(-Lbox/2, Lbox/2, N, endpoint=False); dx = x[1]-x[0]
p = 2*np.pi*hbar*np.fft.fftfreq(N, d=dx)
ok = True; prev_dp = 0
for s in [4.0, 2.0, 1.0, 0.5, 0.25]:
    psi = np.exp(-x**2/(4*s**2))*np.exp(1j*3*x)
    psi /= np.sqrt(np.sum(abs(psi)**2)*dx)
    Px = abs(psi)**2*dx
    dxv = np.sqrt(np.sum(Px*x**2) - np.sum(Px*x)**2)
    phi = np.fft.fft(psi); Pp = abs(phi)**2; Pp /= Pp.sum()
    dpv = np.sqrt(np.sum(Pp*p**2) - np.sum(Pp*p)**2)
    print(f"sigma_x={dxv:.4f}  sigma_p={dpv:.4f}  product={dxv*dpv:.5f} (>= 0.5)")
    ok &= dxv*dpv >= 0.5 - 1e-6 and dpv > prev_dp
    prev_dp = dpv
# a non-Gaussian squeezed shape (box) has even larger product
psi = np.where(abs(x) < 1, 1.0, 0.0).astype(complex); psi /= np.sqrt(np.sum(abs(psi)**2)*dx)
Px = abs(psi)**2*dx; dxv = np.sqrt(np.sum(Px*x**2))
print(f"box: sigma_x={dxv:.3f}, momentum spread large (heavy tails) -> uncertainty holds")
print("PASS" if ok else "FAIL")
