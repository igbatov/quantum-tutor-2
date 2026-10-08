# Claim: "an electron can't have both a sharply pinned-down position and a sharply defined motion" -- "a fact about waves"
# Check: Fourier trade-off: for Gaussian packets of varying width, dx*dp = hbar/2 independent of width (and >= hbar/2 otherwise).
import numpy as np
hbar = 1.0
x = np.linspace(-200, 200, 2**16); dxg = x[1]-x[0]
p = 2*np.pi*hbar*np.fft.fftshift(np.fft.fftfreq(x.size, d=dxg))
res = []
for s in (0.5, 1, 2, 5):
    psi = np.exp(-x**2/(4*s**2))*np.exp(1j*3*x)
    psi /= np.sqrt(np.sum(abs(psi)**2)*dxg)
    px = abs(psi)**2*dxg
    sx = np.sqrt(np.sum(px*x**2)-np.sum(px*x)**2)
    phi = np.fft.fftshift(np.fft.fft(psi)); pp = abs(phi)**2; pp /= pp.sum()
    sp_ = np.sqrt(np.sum(pp*p**2)-np.sum(pp*p)**2)
    res.append((s, sx, sp_, sx*sp_))
for r in res: print("width %.1f: dx=%.4f dp=%.4f dx*dp=%.4f" % r)
# a non-Gaussian (box) wave: product larger
ok = all(abs(r[3]-0.5) < 1e-3 for r in res) and res[0][2] > res[-1][2]
print("PASS" if ok else "FAIL")
