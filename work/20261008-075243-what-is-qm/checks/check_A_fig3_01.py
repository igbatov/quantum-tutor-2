# Claim checked: the Fresnel-integral field used for figure a-three-distances is a correct
# paraxial propagation (cross-check against an independent FFT angular-spectrum propagation).
import numpy as np
from scipy.special import fresnel
a, d = 1.0, 4.0
def u(x, c, lL):
    s = np.sqrt(2/lL); S1, C1 = fresnel(s*(c-a/2-x)); S2, C2 = fresnel(s*(c+a/2-x))
    return ((C2-C1) + 1j*(S2-S1))/np.sqrt(2j)
ok = True
for N in (20, 4, 0.05):
    lL = d*d/N
    W = 40*max(lL/a, 8.0); n = 2**22
    x = (np.arange(n)-n//2)*(2*W/n)
    u0 = ((abs(x+d/2) <= a/2) | (abs(x-d/2) <= a/2)).astype(complex)
    f = np.fft.fftfreq(n, d=2*W/n)
    uL = np.fft.ifft(np.fft.fft(u0)*np.exp(-1j*np.pi*lL*f**2))
    xs = np.linspace(-min(3*lL/a, 3*lL/a)-4, 3*lL/a+4, 2001)
    ref = np.interp(xs, x, abs(uL)**2)
    fr = abs(u(xs, -d/2, lL) + u(xs, d/2, lL))**2
    err = np.max(abs(ref-fr))/fr.max()
    print(f"N={N}: max |FFT - Fresnel| / peak = {err:.2e}")
    ok &= err < 2e-2
print("PASS" if ok else "FAIL", "(tolerance 2% of peak; FFT has finite sampling of the sharp slit edges)")
